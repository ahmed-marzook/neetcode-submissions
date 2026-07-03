static class Singleton {

    private static Singleton singletonInstance = null;

    private String value = null;

    private Singleton() {
    }

    public static Singleton getInstance() {
        if(singletonInstance == null) {
            singletonInstance = new Singleton();
        }
        return singletonInstance;
    }

    public String getValue() {
        return this.value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    
}
