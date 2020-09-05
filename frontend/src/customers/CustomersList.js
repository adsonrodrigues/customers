import React from 'react';
import {useEffect, useState} from "react";
import getAllCustomers from "../utils/api";

function CustomersList() {

    const [customers, setCustomers] = useState([]);

    useEffect( () => {
        async function fetchApi() {
            const { results } = await getAllCustomers();

            setCustomers(results);
        }

        fetchApi();
    }, []);


    return (
        <ul>
            {customers.map((customer) => {
                 return <li key={customer.id}> {customer.first_name} </li>
            })}
        </ul>
    );
}

export default CustomersList;

