interface Observer {
    void notify(String itemName);
}

class Customer implements Observer {
    private String name;
    private int notifications;

    public Customer(String name) {
        this.name = name;
        this.notifications = 0;
    }

    public void notify(String itemName) {
        this.notifications += 1;
    }

    public int countNotifications() {
        return this.notifications;
    }  
}

class OnlineStoreItem {
    private String itemName;
    private int stock;
    private List<Observer> customers = new ArrayList();

    public OnlineStoreItem(String itemName, int stock) {
        this.itemName = itemName;
        this.stock = stock;
    }

    public void subscribe(Observer observer) {
        customers.add(observer);
    }

    public void unsubscribe(Observer observer) {
        customers.remove(observer);
    }

    public void updateStock(int newStock) {
        int oldStock = this.stock;
        this.stock = newStock;
        if(this.stock > 0 && oldStock == 0) {
            notifyCustomers();
        }
    }

    private void notifyCustomers(){
        for(Observer customer : this.customers) {
            customer.notify(this.itemName);
        }
    }
}
