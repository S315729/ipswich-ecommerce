# STEP 1: PLANNING PHASE - DOCUMENTATION

**Date:** November 12, 2025  
**Student ID:** S315729  
**Project:** Ipswich Retail E-commerce DevOps Implementation

---

## 1.1 ARCHITECTURE DIAGRAM

### System Architecture Overview

**Tool Used:** Draw.io (https://app.diagrams.net/)

### Components to Include in Diagram:

```
┌─────────────────────────────────────────────────────────────────┐
│                         USER LAYER                               │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐          │
│  │   Customers  │  │   Admin User │  │  Developers  │          │
│  └──────────────┘  └──────────────┘  └──────────────┘          │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│                    PRESENTATION LAYER                            │
│                  Web Browser (Chrome/Firefox)                    │
│                    Responsive Bootstrap UI                       │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│                   APPLICATION LAYER (MVT)                        │
│  ┌────────────────────────────────────────────────────────┐    │
│  │           Django E-commerce Application                 │    │
│  │  ┌──────────┐  ┌──────────┐  ┌───────────┐           │    │
│  │  │  Models  │  │   Views  │  │ Templates │           │    │
│  │  ├──────────┤  ├──────────┤  ├───────────┤           │    │
│  │  │ Products │  │ Product  │  │   Base    │           │    │
│  │  │   Cart   │  │   Cart   │  │  Product  │           │    │
│  │  │  Orders  │  │  Orders  │  │   Cart    │           │    │
│  │  └──────────┘  └──────────┘  └───────────┘           │    │
│  └────────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│                       DATA LAYER                                 │
│  ┌────────────────────────────────────────────────────────┐    │
│  │        SQLite Database (Dev/Test)                       │    │
│  │     PostgreSQL Database (Production)                    │    │
│  │  ┌──────────┐  ┌──────────┐  ┌───────────┐           │    │
│  │  │Categories│  │ Products │  │Cart/Orders│           │    │
│  │  └──────────┘  └──────────┘  └───────────┘           │    │
│  └────────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│                     DEVOPS PIPELINE                              │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐       │
│  │   Git/   │→ │ GitHub   │→ │  Docker  │→ │PythonAny │       │
│  │  GitHub  │  │ Actions  │  │Container │  │  where   │       │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘       │
│       ↓             ↓             ↓              ↓              │
│    Version      Automated    Containerized   Production         │
│    Control         CI/CD      Environment    Deployment         │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│                  MONITORING & FEEDBACK                           │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐                      │
│  │  GitHub  │  │  Django  │  │   User   │                      │
│  │  Issues  │  │  Logs    │  │ Feedback │                      │
│  └──────────┘  └──────────┘  └──────────┘                      │
└─────────────────────────────────────────────────────────────────┘
```

### Architecture Design Decisions:

**1. Django MVT Pattern:**

- Chose Django over Flask for built-in admin panel and ORM
- MVT provides clear separation of concerns
- Scalable architecture for future growth

**2. Database Strategy:**

- SQLite for development (lightweight, no setup)
- PostgreSQL for production (ACID compliant, robust)
- Easy migration path between environments

**3. DevOps Tools:**

- GitHub: Industry-standard version control
- GitHub Actions: Integrated CI/CD, no extra infrastructure
- Docker: Consistent environments across dev/staging/prod
- PythonAnywhere: Free hosting, Python-native platform

**4. Frontend:**

- Bootstrap 5: Responsive, mobile-first design
- Minimal JavaScript: Focus on server-side rendering
- Progressive enhancement approach

---

## 1.2 WIREFRAME/MOCKUP DOCUMENTATION

### Wireframe Design Tool

**Tool Used:** Draw.io / Figma  
**Design Philosophy:** Simple, clean, user-friendly e-commerce interface

### Page Wireframes:

#### 1. Homepage Wireframe

```
┌─────────────────────────────────────────────────────────────┐
│  Ipswich Retail          [Home] [Products] [Cart] [Login]  │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│        Welcome to Ipswich Retail E-commerce Store           │
│         Your one-stop shop for quality products             │
│                                                              │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │
│  │  Category 1  │  │  Category 2  │  │  Category 3  │     │
│  │ [Electronics]│  │  [Clothing]  │  │   [Books]    │     │
│  └──────────────┘  └──────────────┘  └──────────────┘     │
│                                                              │
│           Featured Products                                  │
│  ┌────────┐  ┌────────┐  ┌────────┐  ┌────────┐          │
│  │ Image  │  │ Image  │  │ Image  │  │ Image  │          │
│  │Product1│  │Product2│  │Product3│  │Product4│          │
│  │ $99.99 │  │ $79.99 │  │ $59.99 │  │ $49.99 │          │
│  │[AddCart]│  │[AddCart]│  │[AddCart]│  │[AddCart]│          │
│  └────────┘  └────────┘  └────────┘  └────────┘          │
│                                                              │
├─────────────────────────────────────────────────────────────┤
│  Footer: © 2025 Ipswich Retail | Contact | Privacy         │
└─────────────────────────────────────────────────────────────┘
```

#### 2. Product List Wireframe

```
┌─────────────────────────────────────────────────────────────┐
│  Ipswich Retail          [Home] [Products] [Cart] [Login]  │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  Products > Electronics                                      │
│                                                              │
│  Filters: [All] [Price: Low-High] [Name: A-Z]              │
│                                                              │
│  ┌────────────┐  ┌────────────┐  ┌────────────┐           │
│  │   Image    │  │   Image    │  │   Image    │           │
│  │  Laptop    │  │  Smartphone│  │  Headphones│           │
│  │  $999.99   │  │  $699.99   │  │  $99.99    │           │
│  │  In Stock  │  │  In Stock  │  │  In Stock  │           │
│  │ [View More]│  │ [View More]│  │ [View More]│           │
│  └────────────┘  └────────────┘  └────────────┘           │
│                                                              │
│  ┌────────────┐  ┌────────────┐  ┌────────────┐           │
│  │   Image    │  │   Image    │  │   Image    │           │
│  │   Tablet   │  │  Keyboard  │  │    Mouse   │           │
│  │  $499.99   │  │  $79.99    │  │  $29.99    │           │
│  │  In Stock  │  │  In Stock  │  │  In Stock  │           │
│  │ [View More]│  │ [View More]│  │ [View More]│           │
│  └────────────┘  └────────────┘  └────────────┘           │
│                                                              │
├─────────────────────────────────────────────────────────────┤
│  Footer: © 2025 Ipswich Retail | Contact | Privacy         │
└─────────────────────────────────────────────────────────────┘
```

#### 3. Product Detail Wireframe

```
┌─────────────────────────────────────────────────────────────┐
│  Ipswich Retail          [Home] [Products] [Cart] [Login]  │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  Home > Products > Electronics > Laptop                      │
│                                                              │
│  ┌─────────────────┐  Professional Gaming Laptop            │
│  │                 │                                         │
│  │                 │  Price: $999.99                        │
│  │  Product Image  │  Stock: 25 Available                   │
│  │   (Large)       │  SKU: ELEC-LAPTOP-001                  │
│  │                 │                                         │
│  │                 │  Category: Electronics                  │
│  └─────────────────┘                                         │
│                      Description:                            │
│  Quantity: [▼ 1]    High-performance laptop with Intel i7   │
│                     16GB RAM, 512GB SSD, RTX 3060 GPU       │
│  [Add to Cart]      Perfect for gaming and productivity     │
│                                                              │
│                     Features:                                │
│                     • 15.6" FHD Display                     │
│                     • Intel Core i7 Processor               │
│                     • NVIDIA RTX 3060 Graphics              │
│                     • 16GB DDR4 RAM                         │
│                     • 512GB NVMe SSD                        │
│                     • Windows 11 Pro                        │
│                                                              │
├─────────────────────────────────────────────────────────────┤
│  Footer: © 2025 Ipswich Retail | Contact | Privacy         │
└─────────────────────────────────────────────────────────────┘
```

#### 4. Shopping Cart Wireframe

```
┌─────────────────────────────────────────────────────────────┐
│  Ipswich Retail          [Home] [Products] [Cart] [Login]  │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  Your Shopping Cart (3 items)                               │
│                                                              │
│  ┌────────────────────────────────────────────────────┐    │
│  │ [Image] Laptop          Qty: [▼2]  $1,999.98  [X] │    │
│  │         Professional Gaming Laptop                  │    │
│  └────────────────────────────────────────────────────┘    │
│                                                              │
│  ┌────────────────────────────────────────────────────┐    │
│  │ [Image] Mouse           Qty: [▼1]    $29.99   [X] │    │
│  │         Wireless Gaming Mouse                       │    │
│  └────────────────────────────────────────────────────┘    │
│                                                              │
│  ┌────────────────────────────────────────────────────┐    │
│  │ [Image] Headphones      Qty: [▼1]    $99.99   [X] │    │
│  │         Noise Cancelling Headphones                 │    │
│  └────────────────────────────────────────────────────┘    │
│                                                              │
│                                       Subtotal: $2,129.96    │
│  [Continue Shopping]                  Tax (10%): $213.00    │
│                                       ─────────────────      │
│                          [Proceed to Checkout] Total: $2,342.96 │
│                                                              │
├─────────────────────────────────────────────────────────────┤
│  Footer: © 2025 Ipswich Retail | Contact | Privacy         │
└─────────────────────────────────────────────────────────────┘
```

### Design Rationale:

**User Experience:**

- Clean navigation: 4 main menu items
- Prominent "Add to Cart" buttons
- Visual product cards with images
- Clear pricing and stock information
- Mobile-responsive grid layout

**Color Scheme:**

- Primary: Bootstrap Blue (#0d6efd)
- Secondary: Gray for text
- Success: Green for "In Stock"
- Warning: Orange for low stock

**Typography:**

- Headers: Sans-serif, bold
- Body: Sans-serif, regular
- Prices: Large, emphasized

---

## 1.3 TEAM COMPOSITION DIAGRAM

### DevOps Team Structure

```
                    ┌─────────────────────┐
                    │   Product Owner     │
                    │  Sarah Thompson     │
                    │ - Define features   │
                    │ - Prioritize backlog│
                    │ - Stakeholder comms │
                    └──────────┬──────────┘
                               │
                    ┌──────────▼──────────┐
                    │   Scrum Master      │
                    │    James Wilson     │
                    │ - Facilitate agile  │
                    │ - Remove blockers   │
                    │ - Team coaching     │
                    └──────────┬──────────┘
                               │
        ┌──────────────────────┼──────────────────────┐
        │                      │                      │
┌───────▼────────┐   ┌────────▼────────┐   ┌─────────▼────────┐
│  Developers    │   │ DevOps Engineer │   │   QA Engineer    │
│  (2-3 people)  │   │   Alex Chen     │   │   Maria Garcia   │
├────────────────┤   ├─────────────────┤   ├──────────────────┤
│ Emma Roberts   │   │ - CI/CD pipeline│   │ - Test planning  │
│ - Frontend     │   │ - Infrastructure│   │ - Automated tests│
│ - Django temps │   │ - Docker/K8s    │   │ - Quality gates  │
│                │   │ - Monitoring    │   │ - Bug tracking   │
│ Michael Lee    │   │ - Security      │   │ - Documentation  │
│ - Backend API  │   │ - Performance   │   │                  │
│ - Database     │   │ - Deploy process│   │                  │
│                │   │                 │   │                  │
│ David Kumar    │   │                 │   │                  │
│ - Full-stack   │   │                 │   │                  │
│ - Integration  │   │                 │   │                  │
└────────────────┘   └─────────────────┘   └──────────────────┘
```

### Team Roles & Responsibilities:

#### 1. Product Owner - Sarah Thompson

**Key Responsibilities:**

- Define product vision and roadmap
- Prioritize feature backlog based on business value
- Accept/reject completed work
- Communicate with stakeholders
- Represent customer needs

**Why Critical for DevOps:**
Breaking down silos requires clear business priorities. The PO ensures development efforts align with customer value, enabling faster feedback loops.

#### 2. Scrum Master - James Wilson

**Key Responsibilities:**

- Facilitate daily standups, sprint planning, retrospectives
- Remove impediments blocking the team
- Coach team on agile and DevOps practices
- Foster collaborative culture
- Track metrics (velocity, lead time)

**Why Critical for DevOps:**
DevOps is cultural transformation. The Scrum Master facilitates communication between traditionally siloed dev and ops, promoting shared ownership.

#### 3. Developers (2-3 People)

**Emma Roberts - Frontend Developer**

- Build responsive UI with Bootstrap
- Implement Django templates
- Client-side validation
- Accessibility compliance

**Michael Lee - Backend Developer**

- Design database models
- Implement business logic in views
- API development
- Performance optimization

**David Kumar - Full-Stack Developer**

- Bridge frontend and backend
- Integration testing
- Code reviews
- Mentoring junior developers

**Why Critical for DevOps:**
Cross-functional developers who understand both code and operations enable "you build it, you run it" philosophy. They write testable, deployable code.

#### 4. DevOps Engineer - Alex Chen

**Key Responsibilities:**

- Design and maintain CI/CD pipelines
- Infrastructure as Code (IaC)
- Container orchestration (Docker/Kubernetes)
- Monitoring and alerting setup
- Security best practices
- Deployment automation
- Performance tuning

**Why Critical for DevOps:**
The dedicated DevOps engineer bridges development and operations, ensuring smooth automated deployments, infrastructure reliability, and rapid feedback.

#### 5. QA Engineer - Maria Garcia

**Key Responsibilities:**

- Test strategy and planning
- Write automated tests (unit, integration, e2e)
- Quality gates in CI/CD pipeline
- Bug tracking and triage
- Load and performance testing
- Documentation of test cases

**Why Critical for DevOps:**
Automated testing in CI/CD ensures quality at speed. QA is integrated from the start (shift-left), catching bugs early rather than after deployment.

---

### Team Size Justification

**Why 6-7 people?**

✅ **Small enough for:**

- Quick decision-making
- Direct communication
- Minimal coordination overhead
- Agile ceremonies under 1 hour

✅ **Large enough for:**

- Coverage across all disciplines
- Redundancy (no single point of knowledge)
- Sustainable pace (vacation/sick coverage)
- Parallel work streams

**Comparison to Traditional Structure:**

| Traditional                        | DevOps Team            |
| ---------------------------------- | ---------------------- |
| Dev team: 10+ people               | Cross-functional: 6-7  |
| Ops team: 5+ people (separate)     | Integrated DevOps      |
| QA team: 3+ people (testing phase) | QA embedded from start |
| Manual handoffs                    | Automated pipeline     |
| Weeks to deploy                    | Minutes to deploy      |
| Finger-pointing                    | Shared ownership       |

---

## 1.4 PROJECT MANAGEMENT - TRELLO BOARD

### Trello Board Structure

**Board Name:** Ipswich Retail DevOps Implementation

### Lists (Columns):

1. **Backlog** - Future work items
2. **To Do** - Ready for current sprint
3. **In Progress** - Active development
4. **Code Review** - Awaiting peer review
5. **Testing** - QA validation
6. **Done** - Completed and deployed

### Sample Cards:

#### BACKLOG:

- Performance optimization
- Advanced search filters
- Email notifications
- Multi-currency support
- API for mobile app

#### TO DO (Sprint 1):

- Setup Django project structure
- Create database models (Products, Cart, Orders)
- Build admin panel
- Design homepage template
- Setup GitHub repository

#### IN PROGRESS:

- Implement shopping cart functionality (Emma)
- Configure CI/CD pipeline with GitHub Actions (Alex)
- Write unit tests for models (Maria)

#### CODE REVIEW:

- Product listing view implementation (Michael)
- Cart calculation logic (Emma)

#### TESTING:

- Order placement workflow (Maria)
- Responsive design on mobile devices (Emma)

#### DONE:

- Initial project setup ✓
- Database schema design ✓
- Git branching strategy defined ✓
- Development environment configured ✓

### Card Details Example:

**Card: "Implement Shopping Cart Functionality"**

- **Assigned to:** Emma Roberts
- **Due Date:** November 13, 2025
- **Labels:** High Priority, Backend, Sprint 1
- **Checklist:**
  - [x] Create Cart model
  - [x] Create CartItem model
  - [x] Implement add_to_cart view
  - [x] Implement remove_from_cart view
  - [x] Implement update_quantity view
  - [x] Create cart_detail template
  - [ ] Write unit tests
  - [ ] Test edge cases (empty cart, stock limits)
- **Comments:**
  - Alex: "Make sure cart persists across sessions"
  - Emma: "Added session-based cart for anonymous users"
  - Maria: "Will test with different quantities tomorrow"

### Agile Sprint Planning:

**Sprint Duration:** 2 weeks  
**Sprint Goal:** MVP e-commerce functionality with DevOps pipeline

**Sprint 1 Focus (Nov 12-25):**

- Core e-commerce features
- Basic CI/CD pipeline
- Docker containerization
- Initial deployment

**Sprint 2 Focus (Nov 26-Dec 9):**

- Enhanced testing coverage
- Monitoring and logging
- Performance optimization
- Security hardening

---

## 1.5 TOOLS SELECTION & JUSTIFICATION

### Version Control: Git + GitHub

**Why chosen:**

- Industry standard version control
- Free for public repositories
- Excellent collaboration features (PR, code review)
- Integrated with CI/CD tools
- Large community support

**Alternatives considered:**

- GitLab: Good but requires more setup
- Bitbucket: Less community adoption
- Azure DevOps: Overkill for this project

### CI/CD: GitHub Actions

**Why chosen:**

- Native GitHub integration
- Free for public repositories
- YAML-based configuration (easy to learn)
- Large marketplace of actions
- No separate infrastructure needed

**Alternatives considered:**

- Jenkins: Powerful but requires separate server, more complex setup
- GitLab CI: Good but would require migrating from GitHub
- CircleCI: Limited free tier
- Travis CI: Pricing changes made it less attractive

### Containerization: Docker

**Why chosen:**

- Industry standard for containers
- Ensures "works on my machine" consistency
- Easy local development setup
- Lightweight compared to VMs
- Excellent documentation

**Alternatives considered:**

- Podman: Less mature ecosystem
- LXC: Lower-level, more complex
- Virtual Machines: Too heavy, slow startup

### Deployment: PythonAnywhere

**Why chosen:**

- FREE tier (no credit card required!)
- Python/Django native support
- Easy deployment process
- Good for PoC and learning
- Web-based console access

**Alternatives considered:**

- Heroku: Now requires credit card, more expensive
- Railway: Limited free tier hours
- AWS/Azure: Too complex for PoC, requires credit card
- DigitalOcean: Requires payment

### Project Management: Trello

**Why chosen:**

- Intuitive Kanban board interface
- Free for small teams
- Easy to learn
- Mobile apps available
- Good GitHub integration

**Alternatives considered:**

- Jira: Too complex, expensive
- Asana: Overkill for small project
- GitHub Projects: Less visual

---

## SCREENSHOTS CHECKLIST FOR PLANNING PHASE

**Please take the following screenshots:**

### Architecture Diagram:

- [ ] **Screenshot 01:** Complete architecture diagram from Draw.io showing all layers

### Wireframes:

- [ ] **Screenshot 02:** Homepage wireframe
- [ ] **Screenshot 03:** Product list wireframe
- [ ] **Screenshot 04:** Product detail wireframe
- [ ] **Screenshot 05:** Shopping cart wireframe

### Team Composition:

- [ ] **Screenshot 06:** Team composition diagram with roles and responsibilities

### Project Management:

- [ ] **Screenshot 07:** Trello board overview with all lists
- [ ] **Screenshot 08:** Sample cards in different columns
- [ ] **Screenshot 09:** Detailed view of one card showing checklist and comments

---

## NEXT STEPS

After completing the planning phase:

1. ✅ Create architecture diagrams (Draw.io)
2. ✅ Design wireframes (Figma/Draw.io)
3. ✅ Document team structure
4. ✅ Setup Trello board (optional)
5. ⏭️ **NEXT:** Environment setup and Git configuration

**Status:** Planning documentation complete! Ready for implementation phase.

---

**Notes for Report:**

- Planning reduces rework and saves time
- Visual diagrams improve stakeholder communication
- Agile methodology with 2-week sprints
- Cross-functional team breaks traditional silos
- Tool selection balanced cost, ease of use, and learning value
