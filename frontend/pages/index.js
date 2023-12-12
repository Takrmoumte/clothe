import React from "react";
import Banner from "./layouts/Fashion/Components/Banner";
import CollectionBanner from "./layouts/Fashion/Components/Collection-Banner";
import TopCollection from "../components/common/Collections/Collection3";
import Parallax from "./layouts/Fashion/Components/Parallax";
import SpecialProducts from "../components/common/Collections/TabCollection1";
import ServiceLayout from "../components/common/Service/service1";
import Blog from "../components/common/Blog/blog1";
import Instagram from "../components/common/instagram/instagram1";
import LogoBlock from "../components/common/logo-block";
import HeaderOne from "../components/headers/header-one";
import { Product4 } from "../services/script";
import Paragraph from "../components/common/Paragraph";
import ModalComponent from "../components/common/Modal";
import Helmet from "react-helmet";
import MasterFooter from "../components/footers/common/MasterFooter";
import Layout from "../components/layout";
import axios from "axios";
import { useEffect, useState } from "react";

const Fashion = () => {

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
  }, []); // Le tableau de dépendances vide signifie que cet effet s'exécute une fois au montage

  

  return (
    <>
    <Layout>
      
      {/* <ModalComponent /> */}

      <Banner />
      <CollectionBanner />
      <Paragraph title="title1 section-t-space" inner="title-inner1" hrClass={false} />
      <TopCollection noTitle="null" backImage={true} type="fashion" title="top collection" subtitle="special offer" productSlider={Product4} designClass="section-b-space p-t-0 ratio_asos px-2" noSlider="false" cartClass="cart-info cart-wrap" dressList={dressList} />
      <Parallax />
      <SpecialProducts type="fashion" backImage={true} productSlider={Product4} line={true} title="title1 section-t-space" inner="title-inner1" designClass="section-b-space p-t-0 ratio_asos" noSlider="true" cartClass="cart-info cart-wrap" />
      <ServiceLayout sectionClass="border-section small-section" />
      <Blog type="fashion" title="title1" inner="title-inner1" />
      <Instagram type="fashion" />
      <div className="section-b-space">
        <LogoBlock />
      </div>
      <MasterFooter footerClass={`footer-light`} footerLayOut={"light-layout upper-footer"} footerSection={"small-section border-section border-top-0"} belowSection={"section-b-space light-layout"} newLatter={true} logoName={"logo.png"} />
    </Layout>
    </>
  );
};

export default Fashion;
