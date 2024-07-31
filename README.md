# Gandalf

Gandalf is an AI regulatory assistant to help medical device and pharmaceutical companies bring their products to market faster by pre-checking their documentation before FDA submission. Upload your PDF and receive a comprehensive review in seconds.

Attention: This is a work in progress and not yet ready for production use.
The frontend (React) and backend (Python) are currently not communicating with each other.

## Contributing

We are actively looking for passionate contributors to join our journey in revolutionizing the regulatory process for medical devices and pharmaceuticals. Whether you're a seasoned developer, a regulatory expert, or someone who loves to tinker with AI, we would love to have you on board!

### How to Contribute

1. Fork the repository
2. Create a new branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

Feel free to check out the open issues and start working on them. If you have any questions or need guidance, don't hesitate to reach out. Let's build something amazing together!


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