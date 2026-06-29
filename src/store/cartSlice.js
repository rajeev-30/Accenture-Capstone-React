import { createSlice } from '@reduxjs/toolkit';

const cartSlice = createSlice({
  name: 'cart',
  initialState: {
    items: [],        
  },
  reducers: {
    addToCart: (state, action) => {
      const pizza = action.payload;
      if (pizza.isCustom) {
        state.items.push({ ...pizza, quantity: 1 });
      } else {
        const existing = state.items.find(item => item.id === pizza.id);
        if (existing) {
          existing.quantity += 1;
        } else {
          state.items.push({ ...pizza, quantity: 1 });
        }
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
    clearCart: (state) => {
      state.items = [];
    },
  },
});

export const {
  addToCart,
  removeFromCart,
  incrementQuantity,
  decrementQuantity,
  clearCart,
} = cartSlice.actions;

export const selectCartItems = (state) => state.cart.items;

export const selectCartCount = (state) =>
  state.cart.items.reduce((total, item) => total + item.quantity, 0);

export const selectPizzaSubtotal = (state) =>
  state.cart.items
    .filter(item => !item.isCustom)
    .reduce((total, item) => total + Number(item.price) * item.quantity, 0);

export const selectIngredientsSubtotal = (state) =>
  state.cart.items
    .filter(item => item.isCustom)
    .reduce((total, item) => total + Number(item.price) * item.quantity, 0);

export const selectAggregatedIngredients = (state) => {
  const ingredientMap = {};
  state.cart.items
    .filter(item => item.isCustom && item.selectedIngredients)
    .forEach(item => {
      item.selectedIngredients.forEach(ing => {
        if (ingredientMap[ing.id]) {
          ingredientMap[ing.id].count += item.quantity;
        } else {
          ingredientMap[ing.id] = { ...ing, count: item.quantity };
        }
      });
    });
  return Object.values(ingredientMap);
};

export const selectCartTotal = (state) =>
  selectPizzaSubtotal(state) + selectIngredientsSubtotal(state);

export default cartSlice.reducer;
