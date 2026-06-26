import { Link } from 'react-router-dom';
import { useSelector } from 'react-redux';
import { selectCartCount } from '../store/cartSlice';
import logo from '../assets/logo.jpeg';

const Navbar = () => {
  const cartCount = useSelector(selectCartCount);

  return (
    <nav className="bg-[#1a1a1a] text-white px-6 py-3 flex items-center justify-between shadow-lg sticky top-0 z-50">
      <div className="flex items-center gap-4">
        <Link to="/" className="flex items-center gap-3 no-underline">
          <span className="text-white text-2xl font-bold tracking-wide">Pizzeria</span>
          <img
            src={logo}
            alt="Pizzeria Logo"
            className="w-10 h-10 rounded-full bg-amber-500 p-1"
          />
        </Link>
        <div className="flex items-center gap-6 ml-6">
          <Link
            to="/order"
            className="text-white no-underline hover:text-amber-400 transition-colors duration-200 text-sm font-medium"
          >
            Order Pizza
          </Link>
          <Link
            to="/build"
            className="text-white no-underline hover:text-amber-400 transition-colors duration-200 text-sm font-medium"
          >
            Build Ur Pizza
          </Link>
        </div>
      </div>

      <Link
        to="/cart"
        className="flex items-center gap-2 bg-amber-500 hover:bg-amber-600 text-black font-semibold px-4 py-2 rounded transition-colors duration-200 no-underline text-sm"
      >
        🛒 Shopping Cart
        {cartCount > 0 && (
          <span className="bg-blue-700 text-white text-xs font-bold px-2 py-0.5 rounded ml-1 min-w-[20px] text-center">
            {cartCount}
          </span>
        )}
      </Link>
    </nav>
  );
};

export default Navbar;
