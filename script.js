// script.js

// Function to generate Google My Business posts
function generateGMBPost(content) {
    return `Generate GMB Post: ${content}`;
}

// Function to generate blog content
function generateBlog(title, content) {
    return `Blog Title: ${title}\nContent: ${content}`;
}

// Function to generate SEO meta tags
function generateSEOMeta(title, description) {
    return `<meta name='description' content='${description}'/>\n<title>${title}</title>`;
}

// Function to generate FAQs
function generateFAQs(question, answer) {
    return `Q: ${question} \nA: ${answer}`;
}

// Function to create lead capture forms
function createLeadCaptureForm() {
    return `form {\n    <label for='name'>Name:</label>\n    <input type='text' id='name' name='name'>\n    <label for='email'>Email:</label>\n    <input type='email' id='email' name='email'>\n    <input type='submit' value='Submit'>\n}`;
}