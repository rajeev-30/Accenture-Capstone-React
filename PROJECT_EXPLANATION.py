# ============================================================================
#  PIZZERIA — COMPLETE PROJECT EXPLANATION (Viva Preparation Guide)
# ============================================================================
#  This file explains the ENTIRE project end-to-end: architecture, workflow,
#  every important function, React concepts used, and potential viva questions.
# ============================================================================


# ╔═══════════════════════════════════════════════════════════════════════════╗
# ║                    SECTION 1: PROJECT OVERVIEW                          ║
# ╚═══════════════════════════════════════════════════════════════════════════╝

"""
PROJECT NAME: Pizzeria
PURPOSE:      A React-based pizza ordering web application where users can:
              1. Browse available pizzas (Order Pizza page)
              2. Build a custom pizza by selecting ingredients (Build Your Pizza page)
              3. Manage cart items with quantity adjustments (Cart/Checkout page)
              4. Complete checkout with real-time billing

TECH STACK:
  - React 19        → JavaScript library for building user interfaces
  - Vite 8          → Fast build tool and dev server (alternative to Create React App)
  - React Router 7  → Client-side routing (navigate between pages without page reload)
  - Redux Toolkit   → State management for cart data (global state)
  - Axios           → HTTP client for fetching JSON data
  - Tailwind CSS 4  → Utility-first CSS framework for styling
"""


# ╔═══════════════════════════════════════════════════════════════════════════╗
# ║                    SECTION 2: PROJECT FOLDER STRUCTURE                  ║
# ╚═══════════════════════════════════════════════════════════════════════════╝

"""
rk7940271-CAPSTONE/
│
├── index.html                    ← Entry HTML file (has <div id="root">)
├── vite.config.js                ← Vite configuration (plugins: React + Tailwind)
├── package.json                  ← Dependencies and scripts
│
├── public/
│   └── data/
│       ├── pizzas.json           ← Pizza menu data (6 pizzas)
│       └── ingredients.json      ← Ingredient data (13 ingredients)
│
└── src/
    ├── main.jsx                  ← APPLICATION ENTRY POINT (renders App)
    ├── App.jsx                   ← ROOT COMPONENT (routing setup)
    ├── index.css                 ← Global CSS (Tailwind import)
    │
    ├── assets/
    │   └── logo.jpeg             ← Pizzeria logo image
    │
    ├── store/
    │   ├── store.js              ← Redux store configuration
    │   └── cartSlice.js          ← Redux slice for cart state management
    │
    ├── components/
    │   ├── Navbar.jsx            ← Navigation bar (shared across all pages)
    │   └── Footer.jsx            ← Footer (shared across all pages)
    │
    └── pages/
        ├── Home.jsx              ← Home page (Our Story, Ingredients, Chefs)
        ├── OrderPizza.jsx        ← Order Pizza page (browse & add to cart)
        ├── BuildPizza.jsx        ← Build Your Pizza page (custom pizza)
        └── Cart.jsx              ← Cart/Checkout page (billing & payment)
"""


# ╔═══════════════════════════════════════════════════════════════════════════╗
# ║               SECTION 3: APPLICATION STARTUP FLOW                       ║
# ╚═══════════════════════════════════════════════════════════════════════════╝

"""
When you run `npm run dev`, here's what happens step by step:

STEP 1: Vite reads index.html
  → index.html has: <script type="module" src="/src/main.jsx">
  → This tells the browser to load main.jsx as the entry point

STEP 2: main.jsx executes
  → It imports React, ReactDOM, Redux Provider, BrowserRouter, App
  → It creates a "root" using ReactDOM.createRoot(document.getElementById('root'))
  → It renders the entire app inside this root element

  The component tree looks like this (outermost → innermost):

    <React.StrictMode>            ← Enables extra checks during development
      <Provider store={store}>    ← Makes Redux store available to ALL components
        <BrowserRouter>           ← Enables client-side routing (URL-based navigation)
          <App />                 ← The root component of our application
        </BrowserRouter>
      </Provider>
    </React.StrictMode>

  WHY THIS ORDER MATTERS:
  - Provider MUST wrap everything that needs Redux access
  - BrowserRouter MUST wrap everything that uses <Link> or <Route>
  - StrictMode is outermost — it's only for development warnings

STEP 3: App.jsx renders
  → It renders Navbar (always visible at top)
  → It renders <Routes> which decides WHICH page to show based on URL
  → It renders Footer (always visible at bottom)

  Routes mapping:
    URL "/"       → renders <Home />          (Home page)
    URL "/order"  → renders <OrderPizza />    (Order Pizza page)
    URL "/build"  → renders <BuildPizza />    (Build Your Pizza page)
    URL "/cart"   → renders <Cart />          (Shopping Cart page)
"""


# ╔═══════════════════════════════════════════════════════════════════════════╗
# ║               SECTION 4: CONFIGURATION FILES EXPLAINED                  ║
# ╚═══════════════════════════════════════════════════════════════════════════╝

"""
─────────────────────────────────
FILE: vite.config.js
─────────────────────────────────
  import { defineConfig } from 'vite';
  import react from '@vitejs/plugin-react';
  import tailwindcss from '@tailwindcss/vite';

  export default defineConfig({
    plugins: [react(), tailwindcss()],
  });

  EXPLANATION:
  - defineConfig()    → Helper function for Vite configuration
  - react()           → Plugin that enables JSX transformation and React Fast Refresh
                         (Fast Refresh = changes update in browser without losing state)
  - tailwindcss()     → Plugin that processes Tailwind CSS utility classes

─────────────────────────────────
FILE: package.json (key parts)
─────────────────────────────────
  "scripts": {
    "dev": "vite",           ← Starts development server (localhost:5173)
    "build": "vite build",   ← Creates production-ready bundle in /dist folder
    "preview": "vite preview" ← Preview the production build locally
  }

  "dependencies" (runtime libraries):
    react, react-dom         → Core React library
    react-router-dom         → Routing (navigation between pages)
    @reduxjs/toolkit         → Redux state management (simplified Redux)
    react-redux              → Connects React components to Redux store
    axios                    → HTTP client for data fetching

  "devDependencies" (build-time only):
    vite                     → Build tool
    @vitejs/plugin-react     → React support for Vite
    tailwindcss              → CSS framework
    @tailwindcss/vite        → Tailwind integration with Vite

─────────────────────────────────
FILE: index.css
─────────────────────────────────
  @import "tailwindcss";

  This single line imports ALL of Tailwind CSS (v4 syntax).
  It enables utility classes like: bg-white, text-red-500, flex, p-4, etc.
"""


# ╔═══════════════════════════════════════════════════════════════════════════╗
# ║           SECTION 5: REDUX STATE MANAGEMENT (THE BRAIN)                 ║
# ╚═══════════════════════════════════════════════════════════════════════════╝

"""
Redux is used to manage the CART STATE globally. Without Redux, we'd need to
pass cart data through props from parent to child, which gets messy. Redux
gives us a SINGLE SOURCE OF TRUTH accessible from ANY component.

─────────────────────────────────
FILE: src/store/store.js
─────────────────────────────────

  import { configureStore } from '@reduxjs/toolkit';
  import cartReducer from './cartSlice';

  const store = configureStore({
    reducer: {
      cart: cartReducer,     ← All cart state lives under state.cart
    },
  });

  EXPLANATION:
  - configureStore() creates the Redux store
  - The store has ONE reducer called "cart"
  - This means all cart data is accessed via: state.cart.items, state.cart.ingredients

─────────────────────────────────
FILE: src/store/cartSlice.js
─────────────────────────────────

  This is the MOST IMPORTANT file in the project. It defines:
  1. The initial state (what data the cart holds)
  2. Reducers (functions that modify cart state)
  3. Selectors (functions that READ cart state)

  ┌─────────────────────────────────────────────────────┐
  │                  INITIAL STATE                       │
  ├─────────────────────────────────────────────────────┤
  │  {                                                   │
  │    items: [],         ← Array of pizza objects       │
  │                         Each item has: id, name,     │
  │                         price, image, type, quantity  │
  │                                                      │
  │    ingredients: [],   ← Array of ingredient objects   │
  │                         From "Build Your Pizza" page  │
  │                         Each has: id, tname, price    │
  │  }                                                   │
  └─────────────────────────────────────────────────────┘

  ┌───────────────────────────────────────────────────────────────────────┐
  │                      REDUCER FUNCTIONS (Actions)                      │
  │  These are functions that MODIFY the state.                          │
  │  They are dispatched from components using: dispatch(actionName())   │
  ├───────────────────────────────────────────────────────────────────────┤
  │                                                                      │
  │  1. addToCart(pizza)                                                  │
  │     → Checks if pizza already exists in cart (by id)                 │
  │     → If YES: increments quantity by 1                               │
  │     → If NO:  adds pizza to items[] with quantity: 1                 │
  │     → USED IN: OrderPizza.jsx when user clicks "Add to Cart"         │
  │                                                                      │
  │  2. removeFromCart(id)                                                │
  │     → Filters out the item with matching id from items[]             │
  │     → USED IN: Cart.jsx when user clicks the trash icon 🗑️            │
  │                                                                      │
  │  3. incrementQuantity(id)                                            │
  │     → Finds item by id and adds 1 to quantity                        │
  │     → USED IN: Cart.jsx & OrderPizza.jsx when user clicks "+"        │
  │                                                                      │
  │  4. decrementQuantity(id)                                            │
  │     → Finds item by id and subtracts 1 from quantity                 │
  │     → ONLY if quantity > 1 (prevents going below 1)                  │
  │     → USED IN: Cart.jsx & OrderPizza.jsx when user clicks "-"        │
  │                                                                      │
  │  5. addIngredient(ingredient)                                        │
  │     → Checks if ingredient already exists (prevents duplicates)      │
  │     → If not present, pushes it to ingredients[]                     │
  │     → USED IN: BuildPizza.jsx when user clicks "Build Ur Pizza"      │
  │                                                                      │
  │  6. removeIngredient(id)                                             │
  │     → Filters out ingredient with matching id                        │
  │     → Not actively used in current UI but available for extension     │
  │                                                                      │
  │  7. clearIngredients()                                               │
  │     → Sets ingredients[] to empty array                              │
  │     → Available for future use                                       │
  │                                                                      │
  │  8. clearCart()                                                       │
  │     → Sets BOTH items[] and ingredients[] to empty arrays            │
  │     → USED IN: Cart.jsx when user clicks "Pay" or "Clear"            │
  │                                                                      │
  └───────────────────────────────────────────────────────────────────────┘

  ┌───────────────────────────────────────────────────────────────────────┐
  │                      SELECTOR FUNCTIONS                              │
  │  These are functions that READ the state (without modifying it).     │
  │  They are used in components via: useSelector(selectorName)          │
  ├───────────────────────────────────────────────────────────────────────┤
  │                                                                      │
  │  1. selectCartItems(state)                                           │
  │     → Returns: state.cart.items (array of pizza objects)              │
  │     → USED IN: Cart.jsx, OrderPizza.jsx                              │
  │                                                                      │
  │  2. selectCartIngredients(state)                                     │
  │     → Returns: state.cart.ingredients (array of ingredient objects)   │
  │     → USED IN: Cart.jsx                                              │
  │                                                                      │
  │  3. selectCartCount(state)                                           │
  │     → Returns: total number of items in cart                         │
  │     → Calculated as: sum of all pizza quantities                     │
  │       + 1 if there are any ingredients (custom pizza counts as 1)    │
  │     → USED IN: Navbar.jsx (shopping cart badge number)               │
  │                                                                      │
  │  4. selectPizzaSubtotal(state)                                       │
  │     → Returns: sum of (price × quantity) for all pizzas              │
  │     → Formula: Σ (item.price × item.quantity)                        │
  │     → USED IN: Cart.jsx (pizza subtotal in billing)                  │
  │                                                                      │
  │  5. selectIngredientsSubtotal(state)                                 │
  │     → Returns: sum of all selected ingredient prices                 │
  │     → Formula: Σ (ingredient.price)                                  │
  │     → USED IN: Cart.jsx (ingredients subtotal in billing)            │
  │                                                                      │
  │  6. selectCartTotal(state)                                           │
  │     → Returns: pizzaSubtotal + ingredientsSubtotal                   │
  │     → This is the GRAND TOTAL shown on checkout                      │
  │     → USED IN: Cart.jsx (total in billing + payment alert)           │
  │                                                                      │
  └───────────────────────────────────────────────────────────────────────┘

  KEY CONCEPT — WHY REDUX TOOLKIT USES "MUTATING" SYNTAX:
  In normal Redux, you CANNOT mutate state directly (state.items.push(x) is WRONG).
  But Redux Toolkit uses a library called "Immer" behind the scenes.
  Immer lets you WRITE code that looks like mutation, but internally creates a
  new immutable copy. So `state.items.push(pizza)` is perfectly safe here.
"""


# ╔═══════════════════════════════════════════════════════════════════════════╗
# ║            SECTION 6: SHARED COMPONENTS (Navbar & Footer)               ║
# ╚═══════════════════════════════════════════════════════════════════════════╝

"""
─────────────────────────────────
FILE: src/components/Navbar.jsx
─────────────────────────────────

  PURPOSE: Navigation bar displayed on ALL pages (sticky at top)

  REACT CONCEPTS USED:
  - useSelector()  → Reads cartCount from Redux store
  - <Link to="/">  → React Router's navigation component (no page reload)

  KEY FUNCTIONS/LOGIC:
  ┌────────────────────────────────────────────────────────────────────┐
  │  const cartCount = useSelector(selectCartCount);                   │
  │                                                                    │
  │  This line reads the total cart count from Redux.                   │
  │  Every time cart changes (add/remove), this auto-updates.          │
  │  This is REACTIVE — React re-renders Navbar when count changes.    │
  └────────────────────────────────────────────────────────────────────┘

  CONDITIONAL RENDERING (cart badge):
  ┌────────────────────────────────────────────────────────────────────┐
  │  {cartCount > 0 && (                                               │
  │    <span className="bg-blue-700 ...">                              │
  │      {cartCount}                                                    │
  │    </span>                                                         │
  │  )}                                                                │
  │                                                                    │
  │  The badge only shows when cartCount > 0.                          │
  │  This uses JavaScript's && (short-circuit) for conditional render. │
  └────────────────────────────────────────────────────────────────────┘

  NAVIGATION LINKS:
  - "Pizzeria" + Logo  → Links to "/" (Home page)
  - "Order Pizza"      → Links to "/order"
  - "Build Ur Pizza"   → Links to "/build"
  - "Shopping Cart"    → Links to "/cart"

  WHY <Link> INSTEAD OF <a>?
  - <a href="/order"> would cause a FULL PAGE RELOAD (traditional navigation)
  - <Link to="/order"> does CLIENT-SIDE navigation (only updates the component,
    no reload, much faster, preserves Redux state)

─────────────────────────────────
FILE: src/components/Footer.jsx
─────────────────────────────────

  PURPOSE: Simple footer with copyright text
  RENDERS: "Copyrights @ 2017 Pizzeria . All rights reserved."
  This is a PURE/STATELESS component — no hooks, no state, just JSX.
"""


# ╔═══════════════════════════════════════════════════════════════════════════╗
# ║                SECTION 7: PAGE-BY-PAGE DETAILED BREAKDOWN               ║
# ╚═══════════════════════════════════════════════════════════════════════════╝


# ─────────────────────────────────────────────
# PAGE 1: HOME (src/pages/Home.jsx)
# Route: "/"
# ─────────────────────────────────────────────

"""
  PURPOSE: Landing page with information about Pizzeria

  SECTIONS:
  1. "Our story"     → Company story paragraphs
  2. "Ingredients"   → Image + description (side-by-side layout)
  3. "Our Chefs"     → Description + image (reversed layout using flex-row-reverse)
  4. "45 min delivery" → Image + delivery promise text

  REACT CONCEPTS USED:
  - This is a STATIC/PRESENTATIONAL component
  - No state, no hooks, no data fetching
  - Pure JSX with Tailwind CSS classes

  TAILWIND CLASSES USED (important ones):
  - max-w-4xl mx-auto    → Centers content with max width of ~56rem
  - flex flex-col md:flex-row → Column on mobile, row on desktop (RESPONSIVE)
  - md:flex-row-reverse   → Reverses layout direction on desktop (Chefs section)
  - object-cover          → Image fills container without stretching
  - rounded-lg shadow-md  → Rounded corners and shadow for images

  NO FUNCTIONS TO EXPLAIN — This page is purely presentational.
"""


# ─────────────────────────────────────────────
# PAGE 2: ORDER PIZZA (src/pages/OrderPizza.jsx)
# Route: "/order"
# ─────────────────────────────────────────────

"""
  PURPOSE: Display all available pizzas and allow adding them to cart

  REACT HOOKS USED:
  ┌─────────────────────────────────────────────────────────────────┐
  │  const [pizzas, setPizzas] = useState([]);                      │
  │  → Local state to store pizza data fetched from JSON            │
  │  → Initially empty array, populated after API call              │
  │                                                                 │
  │  const [loading, setLoading] = useState(true);                  │
  │  → Controls loading spinner visibility                          │
  │  → true initially, set to false after data loads                │
  │                                                                 │
  │  const dispatch = useDispatch();                                │
  │  → Gets the dispatch function to send actions to Redux store    │
  │                                                                 │
  │  const cartItems = useSelector(selectCartItems);                │
  │  → Reads current cart items from Redux to show quantity controls │
  └─────────────────────────────────────────────────────────────────┘

  DATA FETCHING (useEffect):
  ┌─────────────────────────────────────────────────────────────────┐
  │  useEffect(() => {                                              │
  │    axios                                                        │
  │      .get('/data/pizzas.json')                                  │
  │      .then((res) => {                                           │
  │        setPizzas(res.data);    ← Store fetched data in state    │
  │        setLoading(false);      ← Hide loading spinner          │
  │      })                                                         │
  │      .catch((err) => {                                          │
  │        console.error('Error loading pizzas:', err);             │
  │        setLoading(false);                                       │
  │      });                                                        │
  │  }, []);   ← Empty dependency array = runs ONCE on mount       │
  │                                                                 │
  │  WHAT IS useEffect?                                             │
  │  → It runs SIDE EFFECTS after the component renders             │
  │  → The empty [] means it only runs ONCE (when component mounts) │
  │  → Perfect for API calls that should happen on page load        │
  │                                                                 │
  │  WHAT IS axios.get()?                                           │
  │  → Makes an HTTP GET request to the given URL                   │
  │  → '/data/pizzas.json' fetches from the public/ folder          │
  │  → Returns a Promise (async operation)                          │
  │  → .then() handles success, .catch() handles errors             │
  └─────────────────────────────────────────────────────────────────┘

  KEY FUNCTIONS:
  ┌─────────────────────────────────────────────────────────────────┐
  │                                                                 │
  │  handleAddToCart(pizza)                                          │
  │  → Called when user clicks "Add to Cart" button                 │
  │  → Dispatches addToCart action with the pizza object             │
  │  → dispatch(addToCart(pizza)) sends it to Redux store            │
  │  → The reducer in cartSlice handles adding/incrementing          │
  │                                                                 │
  │  getCartItem(pizzaId)                                            │
  │  → Finds if a specific pizza is already in the cart              │
  │  → Returns the cart item object (with quantity) or undefined     │
  │  → Used for conditional rendering: if pizza is in cart,          │
  │    show quantity controls (+/-) instead of "Add to Cart" button  │
  │                                                                 │
  └─────────────────────────────────────────────────────────────────┘

  CONDITIONAL RENDERING (Add to Cart vs Quantity Controls):
  ┌─────────────────────────────────────────────────────────────────┐
  │  {cartItem ? (                                                  │
  │    // Show [-] [quantity] [+] controls                          │
  │    // "-" button: if quantity is 1, removes item entirely       │
  │    //             else decrements quantity                       │
  │    // "+" button: increments quantity                            │
  │  ) : (                                                          │
  │    // Show "Add to Cart" button                                 │
  │  )}                                                             │
  │                                                                 │
  │  This is a TERNARY OPERATOR for conditional rendering.          │
  │  If pizza is already in cart → show quantity controls            │
  │  If pizza is NOT in cart    → show Add to Cart button            │
  └─────────────────────────────────────────────────────────────────┘

  VEG/NON-VEG INDICATOR:
  ┌─────────────────────────────────────────────────────────────────┐
  │  pizza.type === 'veg' ? 'border-green-600' : 'border-red-600'  │
  │                                                                 │
  │  → Green square with green dot = Vegetarian                     │
  │  → Red square with red dot = Non-vegetarian                     │
  │  → Uses conditional class names based on pizza.type             │
  └─────────────────────────────────────────────────────────────────┘

  IMAGE ERROR HANDLING:
  ┌─────────────────────────────────────────────────────────────────┐
  │  onError={(e) => {                                              │
  │    e.target.src = 'https://images.unsplash.com/...';            │
  │  }}                                                             │
  │                                                                 │
  │  → If the pizza image URL fails to load (404, broken link),     │
  │    it replaces with a fallback image from Unsplash              │
  │  → This prevents broken image icons in the UI                   │
  └─────────────────────────────────────────────────────────────────┘
"""


# ─────────────────────────────────────────────
# PAGE 3: BUILD YOUR PIZZA (src/pages/BuildPizza.jsx)
# Route: "/build"
# ─────────────────────────────────────────────

"""
  PURPOSE: Let users build a custom pizza by selecting ingredients

  REACT HOOKS USED:
  ┌─────────────────────────────────────────────────────────────────┐
  │  const [ingredients, setIngredients] = useState([]);            │
  │  → Stores all available ingredients fetched from JSON           │
  │                                                                 │
  │  const [selected, setSelected] = useState({});                  │
  │  → Tracks which ingredients are selected (checked)              │
  │  → It's an OBJECT (not array) for O(1) lookup by ingredient.id │
  │  → Example: { 107: {id:107, tname:"Chicken", price:60}, ... }  │
  │                                                                 │
  │  const [loading, setLoading] = useState(true);                  │
  │  → Controls loading spinner                                     │
  │                                                                 │
  │  const dispatch = useDispatch();                                │
  │  → For dispatching Redux actions                                │
  │                                                                 │
  │  const navigate = useNavigate();                                │
  │  → React Router hook for PROGRAMMATIC navigation                │
  │  → navigate('/cart') takes user to Cart page via code           │
  │  → Unlike <Link>, this is used INSIDE event handlers            │
  └─────────────────────────────────────────────────────────────────┘

  DATA FETCHING:
  ┌─────────────────────────────────────────────────────────────────┐
  │  useEffect(() => {                                              │
  │    axios.get('/data/ingredients.json')                           │
  │      .then((res) => { setIngredients(res.data); })              │
  │  }, []);                                                        │
  │                                                                 │
  │  → Same pattern as OrderPizza — fetches on mount                │
  │  → Loads 13 ingredients from public/data/ingredients.json       │
  └─────────────────────────────────────────────────────────────────┘

  KEY FUNCTIONS:
  ┌─────────────────────────────────────────────────────────────────┐
  │                                                                 │
  │  handleToggle(ingredient)                                       │
  │  ─────────────────────────                                      │
  │  → Called when user clicks a CHECKBOX                           │
  │  → TOGGLES the ingredient: adds if not selected, removes if     │
  │    already selected                                             │
  │  → Uses functional state update: setSelected((prev) => {...})   │
  │  → If ingredient.id exists in selected object → delete it       │
  │  → If ingredient.id doesn't exist → add it                     │
  │                                                                 │
  │  handleAdd(ingredient)                                           │
  │  ─────────────────────                                          │
  │  → Called when user clicks the "Add" text button                │
  │  → Only ADDS the ingredient (doesn't toggle off)                │
  │  → Checks if already selected to prevent duplicates             │
  │  → Difference from handleToggle: Add is ONE-WAY (only adds)    │
  │                                                                 │
  │  totalCost (computed value, not a function)                      │
  │  ─────────────────────────────────────────                      │
  │  → Calculated on EVERY RENDER (not stored in state)             │
  │  → Object.values(selected) gets array of selected ingredients   │
  │  → .reduce() sums up all prices                                 │
  │  → This gives REAL-TIME price update as checkboxes change       │
  │  → Example: if Chicken (₹60) + Tomato (₹20) selected → 80      │
  │                                                                 │
  │  handleBuildPizza()                                              │
  │  ──────────────────                                             │
  │  → Called when user clicks "Build Ur Pizza" button               │
  │  → VALIDATION: If no ingredients selected, shows alert & returns │
  │  → For each selected ingredient, dispatches addIngredient()      │
  │    to Redux store                                                │
  │  → After dispatching, navigates to '/cart' using navigate()      │
  │  → The user is taken to Cart page where they see their custom    │
  │    pizza ingredients in the billing summary                      │
  │                                                                 │
  └─────────────────────────────────────────────────────────────────┘

  DYNAMIC PRICING — HOW IT WORKS:
  ┌─────────────────────────────────────────────────────────────────┐
  │  1. User checks "Chicken" checkbox → handleToggle fires         │
  │  2. setSelected updates: { 107: {...Chicken} }                  │
  │  3. React RE-RENDERS the component                               │
  │  4. totalCost recalculates: 0 + 60 = 60                        │
  │  5. UI shows "Total Cost : 60"                                  │
  │                                                                 │
  │  6. User checks "Tomato" → handleToggle fires again             │
  │  7. selected becomes: { 107: {...Chicken}, 108: {...Tomato} }   │
  │  8. totalCost: 60 + 20 = 80                                    │
  │  9. UI instantly shows "Total Cost : 80"                        │
  │                                                                 │
  │  This is REACTIVE PROGRAMMING — state change → automatic UI     │
  │  update. No manual DOM manipulation needed.                     │
  └─────────────────────────────────────────────────────────────────┘

  WHY 'selected' IS AN OBJECT, NOT AN ARRAY:
  ┌─────────────────────────────────────────────────────────────────┐
  │  Using object { [id]: ingredient } instead of array:            │
  │  - O(1) lookup: selected[ingredient.id] is instant              │
  │  - Easy add: selected[id] = ingredient                          │
  │  - Easy remove: delete selected[id]                             │
  │  - Easy check: !!selected[id] → true/false                     │
  │  If we used an array, we'd need .find() for each check = O(n)  │
  └─────────────────────────────────────────────────────────────────┘
"""


# ─────────────────────────────────────────────
# PAGE 4: CART / CHECKOUT (src/pages/Cart.jsx)
# Route: "/cart"
# ─────────────────────────────────────────────

"""
  PURPOSE: Show cart items, allow quantity changes, show billing, handle payment

  THIS PAGE HAS TWO SECTIONS:
  ┌─────────────────────────────────────────────────────────────────┐
  │  LEFT SIDE: "My Cart"              │  RIGHT SIDE: "Billing"    │
  │  ─────────────────────             │  ────────────────────     │
  │  • List of pizzas in cart          │  • Pizza subtotal         │
  │  • Each item shows:               │  • Ingredients subtotal    │
  │    - Image (circular)             │    (expandable/collapsible)│
  │    - Veg/nonveg indicator         │  • Grand total             │
  │    - Name and unit price          │  • Pay button              │
  │    - Quantity controls [-] [n] [+]│  • Clear button            │
  │    - Line total (price × qty)     │                            │
  │    - Delete button (trash icon)   │                            │
  │  • Subtotal at bottom             │                            │
  └─────────────────────────────────────────────────────────────────┘

  REACT HOOKS USED:
  ┌─────────────────────────────────────────────────────────────────┐
  │  const items = useSelector(selectCartItems);                    │
  │  → Array of pizza items from Redux                              │
  │                                                                 │
  │  const ingredients = useSelector(selectCartIngredients);         │
  │  → Array of custom pizza ingredients from Redux                 │
  │                                                                 │
  │  const pizzaSubtotal = useSelector(selectPizzaSubtotal);        │
  │  → Sum of (price × quantity) for all pizzas                     │
  │                                                                 │
  │  const ingredientsSubtotal = useSelector(selectIngredientsSubtotal); │
  │  → Sum of all ingredient prices                                 │
  │                                                                 │
  │  const total = useSelector(selectCartTotal);                    │
  │  → Grand total = pizzaSubtotal + ingredientsSubtotal            │
  │                                                                 │
  │  const dispatch = useDispatch();                                │
  │  → For dispatching cart modification actions                     │
  │                                                                 │
  │  const [showIngredients, setShowIngredients] = useState(false); │
  │  → Controls whether ingredient details are expanded/collapsed   │
  └─────────────────────────────────────────────────────────────────┘

  KEY FUNCTIONS:
  ┌─────────────────────────────────────────────────────────────────┐
  │                                                                 │
  │  handlePay()                                                     │
  │  ────────────                                                   │
  │  → Called when user clicks "Pay" button                         │
  │  → VALIDATION: If cart is empty, shows alert and returns        │
  │  → Shows success alert with total amount                        │
  │  → Dispatches clearCart() to empty the entire cart               │
  │  → In a real app, this would call a payment API                 │
  │                                                                 │
  │  handleClear()                                                   │
  │  ──────────────                                                 │
  │  → Called when user clicks "Clear" button                       │
  │  → Simply dispatches clearCart() to empty cart                   │
  │  → No confirmation dialog (could be added as enhancement)       │
  │                                                                 │
  └─────────────────────────────────────────────────────────────────┘

  QUANTITY CONTROLS (inline dispatches):
  ┌─────────────────────────────────────────────────────────────────┐
  │  "-" button: dispatch(decrementQuantity(item.id))               │
  │  → Reduces quantity by 1 (minimum stays at 1)                   │
  │                                                                 │
  │  "+" button: dispatch(incrementQuantity(item.id))               │
  │  → Increases quantity by 1                                      │
  │                                                                 │
  │  "🗑️" button: dispatch(removeFromCart(item.id))                  │
  │  → Completely removes the item from cart                        │
  └─────────────────────────────────────────────────────────────────┘

  LINE TOTAL CALCULATION (inline):
  ┌─────────────────────────────────────────────────────────────────┐
  │  ₹{(Number(item.price) * item.quantity).toFixed(2)}             │
  │                                                                 │
  │  → Number(item.price) converts price to number (some prices     │
  │    in JSON are strings like "310", "400")                       │
  │  → Multiplied by quantity                                      │
  │  → .toFixed(2) formats to 2 decimal places                     │
  │  → Example: price=290, quantity=2 → ₹580.00                    │
  └─────────────────────────────────────────────────────────────────┘

  EXPANDABLE INGREDIENTS (Accordion Pattern):
  ┌─────────────────────────────────────────────────────────────────┐
  │  onClick={() => setShowIngredients(!showIngredients)}           │
  │                                                                 │
  │  → Toggles boolean state                                        │
  │  → When true: shows list of individual ingredients with prices  │
  │  → Chevron icon (▼) rotates 180° when expanded using CSS:       │
  │    className={showIngredients ? 'rotate-180' : ''}              │
  └─────────────────────────────────────────────────────────────────┘

  BILL CALCULATION FLOW:
  ┌─────────────────────────────────────────────────────────────────┐
  │  Example:                                                       │
  │  Cart has:                                                      │
  │    Paneer Tikka (₹290) × 2 = ₹580                              │
  │    Chicken Italiaona (₹350) × 1 = ₹350                         │
  │  Custom ingredients: Chicken (₹60) + Tomato (₹20) = ₹80        │
  │                                                                 │
  │  Pizza Subtotal    = 580 + 350     = ₹930.00                    │
  │  Ingredients       = 60 + 20       = ₹80.00                    │
  │  ──────────────────────────────────────────                     │
  │  Total             = 930 + 80      = ₹1010.00                  │
  │                                                                 │
  │  All calculations happen in Redux SELECTORS, not in the         │
  │  component. The component just READS the computed values.       │
  └─────────────────────────────────────────────────────────────────┘
"""


# ╔═══════════════════════════════════════════════════════════════════════════╗
# ║                    SECTION 8: COMPLETE DATA FLOW                        ║
# ╚═══════════════════════════════════════════════════════════════════════════╝

"""
  Here's the COMPLETE data flow when a user adds a pizza to cart:

  ┌──────────────────────────────────────────────────────────────────────┐
  │  USER ACTION: Clicks "Add to Cart" on Paneer Tikka                  │
  │       │                                                              │
  │       ▼                                                              │
  │  OrderPizza.jsx: handleAddToCart(pizza) is called                    │
  │       │                                                              │
  │       ▼                                                              │
  │  dispatch(addToCart(pizza)) sends action to Redux store              │
  │       │                                                              │
  │       ▼                                                              │
  │  cartSlice.js: addToCart reducer executes                            │
  │  → Checks: is Paneer Tikka already in state.cart.items?              │
  │    → NO:  state.items.push({ ...pizza, quantity: 1 })               │
  │    → YES: existingItem.quantity += 1                                 │
  │       │                                                              │
  │       ▼                                                              │
  │  Redux store is UPDATED with new state                               │
  │       │                                                              │
  │       ▼                                                              │
  │  ALL components using useSelector() are NOTIFIED                     │
  │       │                                                              │
  │       ├─→ Navbar.jsx: selectCartCount changes → badge updates to "1" │
  │       ├─→ OrderPizza.jsx: selectCartItems changes → shows [-][1][+] │
  │       └─→ Cart.jsx: (when visited) shows Paneer Tikka in cart        │
  └──────────────────────────────────────────────────────────────────────┘

  END-TO-END USER WORKFLOW:
  ┌──────────────────────────────────────────────────────────────────────┐
  │                                                                      │
  │  1. User visits HOME page (/) → reads about Pizzeria                │
  │       │                                                              │
  │  2. User clicks "Order Pizza" → navigates to /order                 │
  │     → Page fetches pizzas.json via axios                             │
  │     → 6 pizza cards displayed in 2-column grid                      │
  │     → User clicks "Add to Cart" on desired pizzas                   │
  │     → Cart badge in navbar updates in real-time                     │
  │       │                                                              │
  │  3. User clicks "Build Ur Pizza" → navigates to /build              │
  │     → Page fetches ingredients.json via axios                        │
  │     → 13 ingredients shown in table with checkboxes                 │
  │     → User checks ingredients → total cost updates dynamically      │
  │     → User clicks "Build Ur Pizza" button                          │
  │     → Selected ingredients dispatched to Redux store                │
  │     → User auto-navigated to /cart                                  │
  │       │                                                              │
  │  4. User is on CART page (/cart)                                    │
  │     → Left panel: sees all cart items with quantity controls         │
  │     → Right panel: sees billing breakdown                           │
  │       - Pizza subtotal (sum of all pizza line totals)               │
  │       - Ingredients subtotal (sum of custom ingredients)             │
  │       - Grand total                                                 │
  │     → User adjusts quantities using +/- buttons                     │
  │     → All totals update in REAL-TIME                                │
  │     → User clicks "Pay" → success alert → cart cleared              │
  │     → OR clicks "Clear" → cart emptied                              │
  │                                                                      │
  └──────────────────────────────────────────────────────────────────────┘
"""


# ╔═══════════════════════════════════════════════════════════════════════════╗
# ║              SECTION 9: REACT CONCEPTS USED IN THIS PROJECT             ║
# ╚═══════════════════════════════════════════════════════════════════════════╝

"""
  ┌───────────────────────────────────────────────────────────────────────┐
  │  CONCEPT              │ WHERE USED              │ PURPOSE             │
  ├───────────────────────┼─────────────────────────┼─────────────────────┤
  │ useState()            │ All pages except Home   │ Local component     │
  │                       │                         │ state management    │
  ├───────────────────────┼─────────────────────────┼─────────────────────┤
  │ useEffect()           │ OrderPizza, BuildPizza   │ Data fetching on   │
  │                       │                         │ component mount     │
  ├───────────────────────┼─────────────────────────┼─────────────────────┤
  │ useSelector()         │ Navbar, OrderPizza, Cart │ Read Redux state   │
  ├───────────────────────┼─────────────────────────┼─────────────────────┤
  │ useDispatch()         │ OrderPizza, BuildPizza,  │ Send actions to    │
  │                       │ Cart                    │ Redux store         │
  ├───────────────────────┼─────────────────────────┼─────────────────────┤
  │ useNavigate()         │ BuildPizza              │ Programmatic route  │
  │                       │                         │ navigation          │
  ├───────────────────────┼─────────────────────────┼─────────────────────┤
  │ <Link>                │ Navbar                  │ Declarative route   │
  │                       │                         │ navigation (no      │
  │                       │                         │ page reload)        │
  ├───────────────────────┼─────────────────────────┼─────────────────────┤
  │ <Routes> + <Route>    │ App.jsx                 │ Route definitions   │
  ├───────────────────────┼─────────────────────────┼─────────────────────┤
  │ Conditional Rendering │ Navbar (badge),          │ Show/hide elements │
  │ (&&, ternary)         │ OrderPizza (cart/add btn)│ based on state      │
  ├───────────────────────┼─────────────────────────┼─────────────────────┤
  │ List Rendering (.map) │ OrderPizza, BuildPizza,  │ Render arrays as   │
  │                       │ Cart                    │ JSX elements        │
  ├───────────────────────┼─────────────────────────┼─────────────────────┤
  │ Props                 │ Not heavily used because │ Redux handles      │
  │                       │ Redux handles shared     │ data sharing        │
  │                       │ state                   │                     │
  ├───────────────────────┼─────────────────────────┼─────────────────────┤
  │ createSlice()         │ cartSlice.js            │ Redux Toolkit API   │
  │                       │                         │ for reducers        │
  ├───────────────────────┼─────────────────────────┼─────────────────────┤
  │ configureStore()      │ store.js                │ Redux Toolkit API   │
  │                       │                         │ for store creation  │
  └───────────────────────────────────────────────────────────────────────┘
"""


# ╔═══════════════════════════════════════════════════════════════════════════╗
# ║          SECTION 10: POTENTIAL VIVA QUESTIONS & ANSWERS                  ║
# ╚═══════════════════════════════════════════════════════════════════════════╝

"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Q1: What is the tech stack of your project?
A:  React 19 with Vite as the build tool, React Router for client-side
    navigation, Redux Toolkit for global state management (cart), Axios
    for HTTP data fetching, and Tailwind CSS for utility-first styling.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Q2: Why did you choose Vite over Create React App?
A:  Vite is significantly faster than CRA for both dev server startup
    and hot module replacement (HMR). CRA uses Webpack which bundles
    everything before serving, while Vite uses native ES modules and
    only transforms files on demand. CRA is also deprecated/unmaintained.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Q3: What is Redux? Why did you use it instead of useState?
A:  Redux is a predictable state container for JavaScript apps. I used
    it because the cart state needs to be shared across multiple components
    (Navbar badge, Order page, Build page, Cart page). Without Redux,
    I'd need to lift state to the top-level component and pass it down
    through multiple layers of props (prop drilling), which is messy.
    Redux provides a SINGLE SOURCE OF TRUTH accessible from anywhere.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Q4: What is Redux Toolkit and how is it different from plain Redux?
A:  Redux Toolkit (RTK) is the official recommended way to write Redux.
    Plain Redux requires: action types, action creators, switch-case
    reducers, and immutable state updates. RTK simplifies this with
    createSlice() which auto-generates action types and creators, and
    uses Immer internally so you can write "mutating" code that is
    actually immutable under the hood.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Q5: Explain the flow when a user adds a pizza to the cart.
A:  1. User clicks "Add to Cart" button in OrderPizza.jsx
    2. handleAddToCart(pizza) function is called
    3. It dispatches addToCart(pizza) action to the Redux store
    4. The addToCart reducer in cartSlice.js checks if the pizza already
       exists in state.cart.items
    5. If yes → increments quantity; if no → pushes new item with quantity=1
    6. Redux store updates → all subscribed components re-render:
       - Navbar badge shows updated count
       - OrderPizza shows quantity controls instead of "Add to Cart"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Q6: How does the dynamic pricing work on the Build Your Pizza page?
A:  The selected ingredients are stored in a local state object called
    'selected' (keyed by ingredient ID). Every time a checkbox changes,
    handleToggle() updates this object. The totalCost variable is computed
    on every render using Object.values(selected).reduce() which sums up
    all selected ingredient prices. Since React re-renders when state
    changes, the "Total Cost" display updates automatically.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Q7: What is useEffect? Why is the dependency array empty []?
A:  useEffect is a React hook for side effects (API calls, DOM updates,
    timers, etc). It runs AFTER the component renders. The empty dependency
    array [] means the effect runs ONLY ONCE when the component first mounts.
    If I removed [], it would run on every re-render (infinite loop for API
    calls). If I put [someVariable], it would run when that variable changes.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Q8: What is the difference between <Link> and useNavigate()?
A:  Both are from React Router for navigation:
    - <Link to="/order"> is a DECLARATIVE approach, used in JSX like an
      <a> tag. The user clicks it and navigates. Used in Navbar.
    - useNavigate() is an IMPERATIVE/PROGRAMMATIC approach, used inside
      JavaScript event handlers. For example, after building a pizza,
      I call navigate('/cart') to redirect the user via code.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Q9: How does the bill calculation work on the Cart page?
A:  All calculations are done via Redux selectors:
    - selectPizzaSubtotal: Σ(item.price × item.quantity) for all pizzas
    - selectIngredientsSubtotal: Σ(ingredient.price) for all custom ingredients
    - selectCartTotal: pizzaSubtotal + ingredientsSubtotal
    These are DERIVED STATE — computed from the raw cart data. Whenever
    the cart items or quantities change, selectors automatically recompute,
    and the Cart component re-renders with updated values.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Q10: What is useSelector and useDispatch?
A:  - useSelector(selectorFn): A React-Redux hook that reads data FROM the
      Redux store. It subscribes to store changes, so the component re-renders
      when the selected data changes. Example: useSelector(selectCartItems)
    - useDispatch(): Returns the dispatch function. Dispatch is how you send
      actions to the Redux store. Example: dispatch(addToCart(pizza))

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Q11: What is the Provider component in main.jsx?
A:  Provider is from react-redux. It wraps the entire app and passes the
    Redux store down through React's context API. Without Provider,
    useSelector and useDispatch hooks wouldn't work because they wouldn't
    know which store to connect to. Think of it as a "bridge" between
    React components and the Redux store.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Q12: What is BrowserRouter?
A:  BrowserRouter is from react-router-dom. It enables client-side routing
    using the browser's History API. It keeps the URL in sync with the UI
    without making server requests. When the URL changes, React Router
    renders the matching <Route> component. This gives a SPA (Single Page
    Application) experience.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Q13: What validation have you implemented?
A:  1. Build Pizza page: Validates that at least one ingredient is selected
       before allowing "Build Ur Pizza" (shows alert otherwise)
    2. Cart page: Validates cart is not empty before payment (shows alert)
    3. Quantity control: decrementQuantity prevents going below 1
    4. Duplicate prevention: addToCart increments quantity instead of adding
       duplicate; addIngredient checks for existing before pushing
    5. Image fallback: onError handler loads fallback image if URL breaks

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Q14: What is Axios? Why not use fetch()?
A:  Axios is a promise-based HTTP client. While fetch() is built into
    browsers, Axios provides several advantages:
    - Automatic JSON parsing (fetch requires res.json())
    - Better error handling (fetch doesn't reject on HTTP errors)
    - Request/response interceptors
    - Simpler syntax for complex requests
    - Automatic request cancellation support

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Q15: What is Tailwind CSS? Why use it?
A:  Tailwind is a utility-first CSS framework. Instead of writing custom
    CSS classes, you compose styles using pre-built utility classes directly
    in JSX. For example: className="bg-white p-4 rounded-lg shadow-md"
    Benefits: rapid development, consistent design, no CSS file maintenance,
    small production bundle (purges unused classes), responsive design
    with prefixes like md: and lg:.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Q16: What is JSX?
A:  JSX (JavaScript XML) is a syntax extension that lets you write HTML-like
    code inside JavaScript. React components return JSX which React transforms
    into React.createElement() calls. JSX allows embedding JavaScript
    expressions inside curly braces {}, like {pizza.name} or {items.map(...)}.
    It's syntactic sugar — not valid JavaScript by itself.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Q17: What is the Virtual DOM?
A:  React maintains a lightweight in-memory copy of the real DOM called
    the Virtual DOM. When state changes, React creates a new Virtual DOM
    tree, compares it with the previous one (diffing), and only updates
    the CHANGED parts of the real DOM (reconciliation). This is why React
    is fast — it minimizes expensive real DOM operations.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Q18: What is the key prop in .map()? Why is it needed?
A:  When rendering lists with .map(), React needs a unique "key" prop on
    each element (like key={pizza.id}). The key helps React identify which
    items changed, were added, or removed during re-renders. Without keys,
    React would re-render the entire list; with keys, it efficiently updates
    only the changed items. Keys should be stable, unique IDs (not array indices).

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Q19: What is React.StrictMode?
A:  StrictMode is a development-only wrapper that:
    - Warns about deprecated lifecycle methods
    - Detects unexpected side effects (renders components twice)
    - Warns about legacy patterns
    It does NOT affect production builds. It's only for catching bugs early.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Q20: How would you improve this project further?
A:  - Add a backend API (Node.js/Express) instead of static JSON
    - Implement user authentication (login/signup)
    - Add a real payment gateway (Razorpay/Stripe)
    - Persist cart to localStorage so it survives page refresh
    - Add search and filter functionality on Order Pizza page
    - Add pizza size selection (small/medium/large)
    - Implement order history page
    - Add form validation on a delivery address form
    - Add unit tests with React Testing Library
    - Deploy to Vercel or Netlify

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""


# ╔═══════════════════════════════════════════════════════════════════════════╗
# ║                SECTION 11: QUICK COMMAND REFERENCE                      ║
# ╚═══════════════════════════════════════════════════════════════════════════╝

"""
  npm run dev          → Start development server (http://localhost:5173)
  npm run build        → Create production build in /dist folder
  npm run preview      → Preview the production build locally
  npm install          → Install all dependencies from package.json
"""
