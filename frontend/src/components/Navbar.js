   // components/Navbar.js
   import Link from 'next/link';
   import React from 'react';

   const Navbar = () => {
     return (
       <nav>
         <ul>
           <li>
             <Link href="/">Home</Link>
           </li>
           <li>
             <Link href="/charts">Charts</Link>
           </li>
           {/* Add more links as needed */}
         </ul>
       </nav>
     );
   };

   export default Navbar;