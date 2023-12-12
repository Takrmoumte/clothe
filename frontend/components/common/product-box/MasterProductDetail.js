import React from "react";

const MasterProductDetail = ({
  product,
  productDetail,
  currency,
  uniqueTags,
  detailClass,
  title,
  des,
  variantChangeByColor,
}) => {
  let RatingStars = [];
  let rating = product.average_rating;
  let fullStars = Math.floor(rating); // Nombre complet d'étoiles
  let hasHalfStar = rating % 1 >= 0.5; // Vérifie s'il faut une demi-étoile

  for (var i = 0; i < 5; i++) {
    if (i < fullStars) {
      // Étoiles pleines
      RatingStars.push(<i className="fa fa-star" key={i}></i>);
    } else if (i === fullStars && hasHalfStar) {
      // Demi-étoile
      RatingStars.push(<i className="fa fa-star-half-o" key={i}></i>);
    } else {
      // Étoiles vides
      RatingStars.push(<i className="fa fa-star-o" key={i}></i>);
    }
  
  }

  return (
    <div className={`product-detail ${productDetail} ${detailClass}`}>
      <div>
        {title !== "Product style 4" ? (
          <div className="rating">{RatingStars}</div>
        ) : (
          ""
        )}
        <h6>{product.title}</h6>
        {des ? <p>{product.description}</p> : ""}
        <h4>
          {product.price }
          {currency.symbol}
          {/* {(
            (product.price - (product.price * product.discount) / 100) *
            currency.value
          ).toFixed(2)} */}
          <del>
            <span className="money">
              {product.price*1.3 }
              {currency.symbol}
              {/* {(product.price * currency.value).toFixed(2)} */}
            </span>
          </del>
        </h4>
{/* 
        {product.variants.map((vari) => {
          var findItem = uniqueTags.find((x) => x.color === vari.color);
          if (!findItem) uniqueTags.push(vari);
        })}

        {product.type === "jewellery" ||
        product.type === "nursery" ||
        product.type === "beauty" ||
        product.type === "electronics" ||
        product.type === "goggles" ||
        product.type === "watch" ||
        product.type === "pets" ? (
          ""
        ) : (
          <>
            {title !== "Product style 4" && uniqueTags[0].color ? (
              <ul className="color-variant">
                {uniqueTags.map((vari, i) => {
                  return (
                    <li
                      className={vari.color}
                      key={i}
                      title={vari.color}
                      onClick={() =>
                        variantChangeByColor(vari.image_id, product.images)
                      }
                    ></li>
                  );
                })}
              </ul>
            ) : (
              ""
            )}
          </>
        )} */}
      </div>
    </div>
  );
};

export default MasterProductDetail;
