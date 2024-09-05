from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Note
from .serializers import NoteSerializer

class CreateNoteView(APIView):
    def post(self, request):
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class ListNotesView(APIView):
#     def get(self, request):
#         notes = Notes.objects.all()
#         serializer = NoteSerializer(notes, many=True)
#         return Response(serializer.data)
class ListNotesView(APIView):


    serializer_class = NoteSerializer
    def get(self, request):
        notes = Note.objects.all().order_by('id')
        serializer = NoteSerializer(notes, many=True)
        print('list of notes')
        print(serializer.data)
        return Response(serializer.data)

class DeleteNoteView(APIView):
    def delete(self, request, pk):
        print('Inside delete')
        note = Note.objects.get(id=pk)


        if  not note:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        note.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
