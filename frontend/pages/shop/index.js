import React, { useState } from 'react';
import CommonLayout from '../../components/shop/common-layout';
// import { withApollo } from '../../helpers/apollo/apollo';
import ProductList from './common/productList';
import { Container, Row} from 'reactstrap';
import FilterPage from './common/filter';
import axios from 'axios';
import { useEffect } from 'react';

const LeftSidebar = () => {

    const [error, setError] = useState(null);
    const [loading, setLoading] = useState(false);
    const [dressList, setDressList] = useState([]);
  
    useEffect(() => {
      const fetchData = async () => {
        setLoading(true);
        try {
          const response = await axios.get('http://localhost:8000/api/dresses/');
         
          setDressList(response.data); 
        } catch (error) {
          setError(error);
        } finally {
          setLoading(false);
        }
       
      };
  
      fetchData();
    }, []);

    const [sidebarView,setSidebarView] = useState(false)
    
    const openCloseSidebar = () => {
        if(sidebarView){
            setSidebarView(!sidebarView)
        } else {
            setSidebarView(!sidebarView)
        }

    }

    console.log('DRESSLIST', dressList)
    return (
        <CommonLayout title="collection" parent="home" >
            <section className="section-b-space ratio_asos">
                <div className="collection-wrapper">
                    <Container>
                        <Row>
                            <FilterPage sm="3"   sidebarView={sidebarView} closeSidebar={() => openCloseSidebar(sidebarView)} />
                            <ProductList dressList={dressList} colClass="col-xl-3 col-6 col-grid-box" layoutList=''  openSidebar={() => openCloseSidebar(sidebarView)}/>
                        </Row>
                    </Container>
                </div>
            </section>
        </CommonLayout>
    )
}

export default LeftSidebar;