let cartItems = [];
let total = 0;

function addToCart(itemName, itemPrice) {
    cartItems.push({ name: itemName, price: itemPrice });
    total += itemPrice;

    
    updateCartDisplay();
}

function updateCartDisplay() {
    const cartList = document.getElementById("cart-items");
    cartList.innerHTML = "";

    cartItems.forEach(item => {
        const li = document.createElement("li");
        li.innerHTML = `
            <span>${item.name}</span>
            <span>$${item.price.toFixed(2)}</span>
        `;
        cartList.appendChild(li);
    });

    document.getElementById("cart-total").textContent = total.toFixed(2);
}

function checkout() {
    if (cartItems.length === 0) {
        alert("Your cart is empty. Please add items to your cart first.");
    } else {
        alert(`Total amount: $${total.toFixed(2)}\nThank you for your order!`);
        
        cartItems = [];
        total = 0;
        updateCartDisplay();
    }
}
