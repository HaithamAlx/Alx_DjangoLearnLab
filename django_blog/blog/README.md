# Blog Post Management Features

## CRUD Operations
- List all posts: `/posts/`
- View post details: `/posts/<int:pk>/`
- Create new post: `/posts/new/` (login required)
- Edit post: `/posts/<int:pk>/edit/` (login & author only)
- Delete post: `/posts/<int:pk>/delete/` (login & author only)

## Permissions
- Only authenticated users can create posts
- Only the author can edit or delete their posts
- List and detail views are public

## Notes
- Author is automatically assigned based on logged-in user
- CSRF protection enabled in all forms
- Forms validate data automatically using Django ModelForm
