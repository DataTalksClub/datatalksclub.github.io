// FAQ Accordion functionality
document.addEventListener('DOMContentLoaded', function() {
    // Initialize all accordions on the page
    const accordions = document.querySelectorAll('.faq-accordion');
    
    accordions.forEach(function(accordion) {
        const items = accordion.querySelectorAll('.faq-item');
        
        items.forEach(function(item) {
            const question = item.querySelector('.faq-question');
            const answer = item.querySelector('.faq-answer');
            
            if (question && answer) {
                // Add click event listener
                question.addEventListener('click', function() {
                    toggleAccordionItem(item, answer);
                });
                
                // Add keyboard support
                question.addEventListener('keydown', function(e) {
                    if (e.key === 'Enter' || e.key === ' ') {
                        e.preventDefault();
                        toggleAccordionItem(item, answer);
                    }
                });
                
                // Add ARIA attributes for accessibility
                question.setAttribute('role', 'button');
                question.setAttribute('aria-expanded', 'false');
                question.setAttribute('tabindex', '0');
                answer.setAttribute('role', 'region');
                answer.setAttribute('aria-labelledby', question.id || generateId(question));
                
                // Generate ID if not present
                if (!question.id) {
                    question.id = generateId(question);
                }
                answer.setAttribute('aria-labelledby', question.id);
            }
        });
    });
});

function toggleAccordionItem(item, answer) {
    const isActive = item.classList.contains('active');
    const question = item.querySelector('.faq-question');
    
    // Close all other items in the same accordion
    const accordion = item.closest('.faq-accordion');
    const allItems = accordion.querySelectorAll('.faq-item');
    
    allItems.forEach(function(otherItem) {
        if (otherItem !== item) {
            otherItem.classList.remove('active');
            const otherQuestion = otherItem.querySelector('.faq-question');
            const otherAnswer = otherItem.querySelector('.faq-answer');
            if (otherQuestion && otherAnswer) {
                otherQuestion.setAttribute('aria-expanded', 'false');
            }
        }
    });
    
    // Toggle current item
    if (isActive) {
        item.classList.remove('active');
        question.setAttribute('aria-expanded', 'false');
    } else {
        item.classList.add('active');
        question.setAttribute('aria-expanded', 'true');
    }
}

function generateId(element) {
    // Generate a unique ID based on the element's text content
    const text = element.textContent.trim().toLowerCase()
        .replace(/[^a-z0-9\s]/g, '')
        .replace(/\s+/g, '-')
        .substring(0, 50);
    return 'faq-' + text + '-' + Math.random().toString(36).substr(2, 9);
}

// Optional: Add smooth scrolling for better UX
function smoothScrollToElement(element) {
    element.scrollIntoView({
        behavior: 'smooth',
        block: 'start'
    });
}
