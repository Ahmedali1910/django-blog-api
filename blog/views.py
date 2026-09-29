from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
# Create your views here.
from .models import Comment,Post,Author,Category


def Welcome (request):
    return HttpResponse("Welcome")


def Posts(request):

      posts = Post.objects.all()
      data =[]

      for post in posts:

        data.append({
            "content":post.content
        })

           
      return JsonResponse({

      
     "posts":data

           
      })

def Specific_Post(request,title):
    post=Post.objects.get(title=title)

    return JsonResponse({

            "content":post.content , 
            "title":post.title,
            "author":post.author.name,
            "category":post.category.name,
            "publication_date":post.publication_date,
            "updated_at":post.updated_at 

     })


def Specific_Author(request,author):
    posts = Post.objects.filter(author__name=author)
    data=[]
    for post in posts:
        data.append({


            "content":post.content , 
            "title":post.title,
            "author":post.author.name,
            "category":post.category.name,
            "publication_date":post.publication_date,
            "updated_at":post.updated_at 
        })
    return JsonResponse({

           "posts":data 

     })

def Specific_Category (request,category):
    posts = Post.objects.filter(category__name=category)
    data=[]
    for post in posts:
            data.append({
    
    
                "content":post.content , 
                "title":post.title,
                "author":post.author.name, # 3lshan post.author btrg3 object lkn post.author.name btrg3 el esm bss
                "category":post.category.name,#nfs el kalam
                "publication_date":post.publication_date,
                "updated_at":post.updated_at 
            })
    return JsonResponse({
    
               "posts":data 
    
         })

def Create (request):
    author,created = Author.objects.get_or_create(name="ahmed")  
    category,created = Category.objects.get_or_create(name="lifestyle") 
    post=Post.objects.create(title="Rookie Moms",author=author,
                             content="Rookie Moms focuses on various products and activities for babies, toddlers, and preschoolers. Like the name says, the site is aimed at new moms who don’t have much experience with parenthood",
                             category=category,
                             publication_date="2010-10-15")
    return JsonResponse({
        "message": "Post created successfully"
    })


def Update (request):
    post2=Post.objects.get(title="Rookie Moms")
    author,created = Author.objects.get_or_create(name="ali")  
    post2.author=author
    post2.save()
    return JsonResponse({
            "message": "Post updated successfully"
        })


def Delete (request):

    post3=Post.objects.get(title="Rookie Moms")
    post3.delete()
    return JsonResponse({
                "message": "Post deleted successfully"
            })

def add_comment (request,id):
    post4=Post.objects.get(id=id)
    comment=Comment.objects.get_or_create(content="First comment",created_at="2025-10-5",post=post4)

    return JsonResponse({
                    "message": " The comment has been successfully added."
                })

def update_comment (request,id):
    post5=Post.objects.get(id=id)
    comment2=Comment.objects.get(post=post5)
    comment2.content="second comment"
    comment2.save()
    return JsonResponse({
                "message": " The comment has been successfully updated."
            })


def delete_comment (request,id):
    post6=Post.objects.get(id=id)
    comment3=Comment.objects.filter(post=post6).first() #aw mmokn ageb el id bta3 el comment
    comment3.delete()

    return JsonResponse({
              "message": " The comment has been successfully deleted."

            })



