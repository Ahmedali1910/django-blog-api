from django.db import models

# Create your models here.

class Category (models.Model):

      name=models.CharField(max_length=20)
      def __str__(self):
            return self.name



class Author (models.Model):
      name=models.CharField(max_length=20)
      email=models.EmailField(null=True)
      def __str__(self):
            return self.name

class Post (models.Model):

      title=models.CharField(max_length=20)
      content=models.TextField()
      category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name='categories')
      author=models.ForeignKey(Author,on_delete=models.CASCADE,related_name='authors')
      publication_date = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)

      def __str__(self):
           return self.title


class Comment (models.Model):
      content=models.TextField()
      created_at=models.DateTimeField(auto_now_add=True)
      post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')  

      