class ShoppingCart:
    def __init__(self):
        self.items = {}
    
    def add_item(self, name, price):
        """Add item to cart or update quantity if exists"""
        if name in self.items:
            self.items[name] += price
        else:
            self.items[name] = price
    
    def remove_item(self, name):
        """Remove item from cart"""
        if name in self.items:
            del self.items[name]
    
    def total_cost(self):
        """Return total cost of all items"""
        return sum(self.items.values())


def test_shopping_cart():
    """Test cases for ShoppingCart"""
    cart = ShoppingCart()
    
    # Test add_item
    cart.add_item("Apple", 10.0)
    cart.add_item("Banana", 5.0)
    assert cart.total_cost() == 15.0, "Test 1 failed"
    print("✓ Test 1: Add items")
    
    # Test add same item again (should add to price)
    cart.add_item("Apple", 10.0)
    assert cart.total_cost() == 25.0, "Test 2 failed"
    print("✓ Test 2: Add duplicate item")
    
    # Test remove_item
    cart.remove_item("Banana")
    assert cart.total_cost() == 20.0, "Test 3 failed"
    print("✓ Test 3: Remove item")
    
    # Test remove non-existent item
    cart.remove_item("Orange")
    assert cart.total_cost() == 20.0, "Test 4 failed"
    print("✓ Test 4: Remove non-existent item")
    
    # Test empty cart
    cart.remove_item("Apple")
    assert cart.total_cost() == 0.0, "Test 5 failed"
    print("✓ Test 5: Empty cart")
    
    print("\nAll tests passed!")


if __name__ == "__main__":
    test_shopping_cart()