from django import template

register = template.Library()

@register.simple_tag
def get_comments_length(comments, id):
  return len(comments[id])

@register.simple_tag
def show_comments(comments, id):
  toRender = ""
  for c in comments[id]:
    toRender += '<p class="comment-body">'
    toRender += c.body
    toRender += '</p>'
  return toRender
