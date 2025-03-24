export interface Transaction {
    id: string;
    type: string;
    amount: number;
    user: string;
    product: string;
    category: string;
    active: boolean;
}