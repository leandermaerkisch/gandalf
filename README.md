# Gandalf

Gandalf is an AI regulatory assistant to help medical device and pharmaceutical companies bring their products to market faster by pre-checking their documentation before FDA submission. Upload your PDF and receive a comprehensive review in seconds.

Attention: This is a work in progress and not yet ready for production use.


# Getting Started
1. Clone the repository

## Getting Started with Frontend

To get the frontend running locally:
1. Navigate to the frontend directory: `cd frontend`
2. Install dependencies: `npm install`
3. Start the development server: `npm run dev`
4. Open your browser and visit `http://localhost:3000`

## Getting Started with Backend

To get the backend running locally:

1. Navigate to the backend directory: `cd backend`
2. Create a virtual environment (optional but recommended): `python -m venv venv`
3. Activate the virtual environment:
   - On Windows: `venv\Scripts\activate`
   - On Unix/Linux/MacOS: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Start the development server: `python demo.py`

## Project Structure

This project uses a custom utility function for merging Tailwind CSS classes. The following file is already included in the project:

- `frontend/lib/utils.ts`

This file contains the following utility function:

```typescript
import { type ClassValue, clsx } from "clsx"
import { twMerge } from "tailwind-merge"

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs))
}
```

Ensure you have the required dependencies installed:

```bash
npm install clsx tailwind-merge
```