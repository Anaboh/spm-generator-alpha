# SPM Generator App

AI-powered document summarization tool for policymakers.

## Deployment Instructions

1. **Create Accounts:**
   - [GitHub](https://github.com)
   - [Hugging Face](https://huggingface.co) (Get API key)
   - [Render](https://render.com)

2. **Upload to GitHub:**
   - Create new repository
   - Upload all files

3. **Deploy Backend:**
   - Go to Render dashboard
   - Create "Web Service"
   - Connect GitHub repository
   - Select `backend` directory
   - Set environment variable: `HF_API_KEY=your_hugging_face_key`
   - Click "Create Web Service"

4. **Deploy Frontend:**
   - In Render dashboard, create "Static Site"
   - Connect GitHub repository
   - Select `frontend` directory
   - Build Command: `npm install && npm run build`
   - Publish Directory: `build`

5. **Configure Frontend:**
   - After deployment, copy backend URL
   - In frontend code, replace `https://your-backend-url.onrender.com` with your actual URL
   - Re-deploy frontend

6. **Access App:**
   - Open frontend URL in browser
   - Upload PDF and generate summaries!
