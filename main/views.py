from django.shortcuts import render, redirect, get_object_or_404
from .models import board
# Create your views here.

def index(request):
    boards = board.objects
    return render(request, 'index.html',{'boards': boards})
    
def new(request):
    return render(request, 'new.html')

def create(request):
    Board = board()
    Board.title = request.GET['title']
    Board.text = request.GET['text']
    Board.save()
    return redirect('/')
    
def read(request, board_id):
    read = get_object_or_404(board, pk = board_id)
    return render(request, 'read.html', {'read': read})


def delete(request, board_id):
    board_target = board.objects.get(id=board_id)
    board_target.delete()
    return redirect('/')
    
def edit(request, board_id):
    board_target = board.objects.get(id=board_id)
    return render(request, 'edit.html', {'board_target':board_target})
    
def update(request):
    Board = board()
    Board.title = request.GET['title']
    Board.text = request.GET['content']
    Board.save()
    return redirect('/')