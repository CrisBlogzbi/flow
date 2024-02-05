# The Flow - Social Blogging Platform

![Flow Header](staticfiles/readme-images/main-page.png)

Welcome to **Flow**, a social blogging platform that lets you express yourself through posts and engage with other users.

## Features

### Blogging Environment

The platform offers a user-friendly environment for creating and exploring blog content. Here's an overview of the key features:

- Navbar with easy access to key actions like creating a new post, signing in, or signing up.
- Post list showcasing titles, content snippets, and post details.
- Post details page revealing the full content, author information, creation time, and the number of comments.
- User authentication for personalized experiences.
- Options for logging in, signing up, or logging out based on user status.
- Responsive design for optimal viewing across devices.

### Post Interaction

- Users can create new posts seamlessly through a dedicated "New Post" button.
- Comment section for each post, allowing users to engage in discussions.
- Number of comments displayed for each post on the main page.
- User-specific actions like logging out or accessing account-related pages.

![Post Interaction](staticfiles/readme-images/post-detail.png)

- The interactive and visually appealing design enhances the overall user experience.

![New Post Hover](staticfiles/readme-images/new-post-hover.png)
![Title Hover](staticfiles/readme-images/post-title-hover.png)

## Styling

### Color Palette

To maintain a vibrant and engaging theme, The Flow embraces a diverse color palette:

- The background, a blend of deep teal, signifies the dynamic and ever-flowing nature of social interactions.
- Post content presented in calming light blue, fostering a sense of open communication and sharing.
- Key action buttons, such as "New Post," are highlighted in a refreshing shade of green, promoting user engagement.

## How to Use

1. **Explore Posts:**
   - Navigate through the main page to discover a curated list of posts.

2. **Create a New Post:**
   - Click on the "New Post" button in the navbar to share your thoughts and stories.
   ![New Post](staticfiles/readme-images/new-post-form.png)

3. **Engage in Discussions:**
   - Access post details to read full content, view comments, and participate in discussions.
   ![Add Comment](staticfiles/readme-images/add-comment.png)

4. **Edit your comments as well as your posts.**

   ![Edit Comment](staticfiles/readme-images/edit-comment.png)
   ![Edit Post](staticfiles/readme-images/edit-post.png)

5. **Or even delete your posts.**

   ![Delete Post](staticfiles/readme-images/delete-post.png)

6. **Authentication:**
   - Log in or sign up to unlock personalized features and connect with the community.
   ![Sign Up Form](staticfiles/readme-images/signup-form.png)
   ![Sign Up Sign in](staticfiles/readme-images/signup-signin.png)

7. **Optimized Experience:**
   - Enjoy a visually appealing and responsive design for an optimal browsing experience.

## Technologies Used

- **Django/Python:** Powering the backend and handling data models.
- **HTML, CSS, JavaScript:** Crafting the frontend and enhancing user interactions.

## Deployment

- Flow is deployed on Heroku and is curently not working. When run locally either by using "python manage.py runserver" or "waitress-serve --host=127.0.0.1 --port=8000 flow.wsgi:application" it works without any issues. I've tried to identify the issue and I still wasn't able to find out the reason why it won't open on Heroku. I've tried asking both Cody and ChatGPT but it was to no use. So the only way to run the code is:

1. Open a New Terminal.
2. Return either "pyhton manage.py runserver" or "waitress-serve --host=127.0.0.1 --port=8000 flow.wsgi:application"
3. CTRL+Left-Click on the link that appears on the terminal.
4. To close the server press CTRL+C.
