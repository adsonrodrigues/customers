export const API_URL = 'http://localhost:8000/api';

export const getAllCustomers = async () => {
    const response = await fetch(`${API_URL}/customers`);

    return response.json();
}

export const getCustomerDetail = () => {

}

export default getAllCustomers