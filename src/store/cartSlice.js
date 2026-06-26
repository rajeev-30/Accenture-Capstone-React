import { createSlice } from '@reduxjs/toolkit';

const cartSlice = createSlice({
  name: 'cart',
  initialState: {
    items: [],        
    ingredients: [],   
  },
  reducers: {
    addToCart: (state, action) => {
      const pizza = action.payload;
      const existing = state.items.find(item => item.id === pizza.id);
      if (existing) {
        existing.quantity += 1;
      } else {
        state.items.push({ ...pizza, quantity: 1 });
      }
    },
    removeFromCart: (state, action) => {
      const id = action.payload;
      state.items = state.items.filter(item => item.id !== id);
    },
    incrementQuantity: (state, action) => {
      const id = action.payload;
      const item = state.items.find(item => item.id === id);
      if (item) {
        item.quantity += 1;
      }
    },
    decrementQuantity: (state, action) => {
      const id = action.payload;
      const item = state.items.find(item => item.id === id);
      if (item && item.quantity > 1) {
        item.quantity -= 1;
      }
    },
    addIngredient: (state, action) => {
      const ingredient = action.payload;
      const existing = state.ingredients.find(i => i.id === ingredient.id);
      if (!existing) {
        state.ingredients.push(ingredient);
      }
    },
    removeIngredient: (state, action) => {
      const id = action.payload;
      state.ingredients = state.ingredients.filter(i => i.id !== id);
    },
    clearIngredients: (state) => {
      state.ingredients = [];
    },
    clearCart: (state) => {
      state.items = [];
      state.ingredients = [];
    },
  },
});

export const {
  addToCart,
  removeFromCart,
  incrementQuantity,
  decrementQuantity,
  addIngredient,
  removeIngredient,
  clearIngredients,
  clearCart,
} = cartSlice.actions;

export const selectCartItems = (state) => state.cart.items;
export const selectCartIngredients = (state) => state.cart.ingredients;
export const selectCartCount = (state) =>
  state.cart.items.reduce((total, item) => total + item.quantity, 0) +
  (state.cart.ingredients.length > 0 ? 1 : 0);

export const selectPizzaSubtotal = (state) =>
  state.cart.items.reduce((total, item) => total + Number(item.price) * item.quantity, 0);

export const selectIngredientsSubtotal = (state) =>
  state.cart.ingredients.reduce((total, ing) => total + Number(ing.price), 0);

export const selectCartTotal = (state) =>
  selectPizzaSubtotal(state) + selectIngredientsSubtotal(state);

export default cartSlice.reducer;
