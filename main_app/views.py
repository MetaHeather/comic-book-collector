from django.shortcuts import render
# Create your views here.

class Comic:  # Note that parens are optional if not inheriting from another class
  def __init__(self, title, issue, author, description, publishdate):
    self.title = title
    self.issue = issue
    self.author = author
    self.description = description
    self.publishdate = publishdate

comics = [
  Comic('Saga', '1', 'Brian K. Vaughan', 'Space war opera', 'Mar 2012'),
  Comic('Preacher', '5', 'Garth Ennis', 'Post appocalyptic situatons', 'Aug 1995'),
  Comic('The Walking Dead', '1', 'Robert Kirkman', 'Zombie appocalypse', 'Oct 2013')
]

# The home view
def home(request):
    return render(request, 'home.html')
# about view
def about(request):
    return render(request, 'about.html')
# comics index
def comics_index(request):
  return render(request, 'comics/index.html', { 'comics': comics })



