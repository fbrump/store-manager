export interface Product {
    id: string;
    code: string;
    name: string;
    description?: string;
    price: number;
    priceCurrency: string;
    category: string;
    active: boolean;
}