# project_kobylan
<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>kobylans site</title>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/hamburgers/1.2.1/hamburgers.css">
  <link rel="stylesheet" href="<?php echo get_template_directory_uri(); ?>/css/style.css">
</head>
<body>

<!-- ----header--------------------------------------------- -->
<header class="header">
<h1>Portfolio Site</h1>
</header>



<!-- sp hamburger-menu ------------------------------------>
<div class="hamburger hamburger--arrowalt">
  <div class="hamburger-box">
    <div class="hamburger-inner"></div>
  </div>
</div>



<!-- ----nav--------------------------------------------- -->
<nav class="g-nav">
<ul>
<li><a href="#profile">Profile</a></li>
<li><a href="#web-site">Web Site</a></li>
<li><a href="#image">Image</a></li>
<li><a href="#other">Other</a></li>
</ul>
</nav>




<main class="main">
<!-- ----profile--------------------------------------------- -->
<section class="contents profile">


<div class="contents-wrapper">

<!-- 表示する投稿記事の種類を限定する -->
<?php
$arg = array('category_name'=>'profile');
$custom_post = new WP_Query($arg);
?>

<?php while($custom_post->have_posts()): ?>
<?php $custom_post->the_post(); ?>
<h2 id="profile"><?php the_title(); ?></h2>
<?php the_content(); ?>

<?php endwhile; ?>

</div><!-- /.contents-wrapper -->
</section><!--  /.profile -->




<!-- --Web Site--------------------------------------------- -->
<section class="contents web-site">
<h2 id="web-site">Web Site</h2>

<div class="contents-wrapper">

<section class="contents-item original">
<h3>Original Site</h3>
<p>授業で学習した内容をベースに自分でデザインしたオリジナルサイトです。</p>

<div class="flex-box original-box">


<!-- 表示する投稿記事の種類を限定する -->
<?php
$arg = array('category_name'=>'web-site');
$custom_post = new WP_Query($arg);
?>

<?php while($custom_post->have_posts()): ?>
<?php $custom_post->the_post(); ?>

<section class="item">
<a href="#">
<h4><?php the_title(); ?></h4>
<?php the_content(); ?>
</a>
</section>
<?php endwhile; ?>


</div><!-- /.flex-box -->
</section> <!-- /.contents-item -->



<section class="contents-item study">
<h3>Study Site</h3>
<p>授業内で作成した演習サイトです。</p>

<div class="flex-box study-box">

<!-- 表示する投稿記事の種類を限定する -->
<?php
$arg = array('category_name'=>'web-study');
$custom_post = new WP_Query($arg);
?>

<?php while($custom_post->have_posts()): ?>
<?php $custom_post->the_post(); ?>

<section class="item">
<a href="#">
<h4><?php the_title(); ?></h4>
<?php the_content(); ?>
</a>
</section>
<?php endwhile; ?>


</div><!--  /.flex-box -->
</section><!-- /.study -->

</div><!-- contents-wrapper -->
</section><!-- /.web-site -->




<!-- --Image--------------------------------------------- -->
<section class="contents image">
<h2 id="image">Image</h2>

<div class="contents-wrapper">

<section class="contents-item original">
<h3>Original Image</h3>
<p>授業で学習した内容をベースに自分でデザインしたオリジナル画像素材です。</p>

<div class="flex-box original-box">

<!-- 表示する投稿記事の種類を限定する -->
<?php
$arg = array('category_name'=>'image-original');
$custom_post = new WP_Query($arg);
?>

<?php while($custom_post->have_posts()): ?>
<?php $custom_post->the_post(); ?>

<section class="item">
<a href="#">
<h4><?php the_title(); ?></h4>
<?php the_content(); ?>
</a>
</section>
<?php endwhile; ?>


</div><!-- /.flex-box -->
</section><!-- /.contents-item -->



<section class="contents-item study">
<h3>Study Image</h3>
<p>授業内で作成した演習画像です。</p>

<div class="flex-box study-box">

<!-- 表示する投稿記事の種類を限定する -->
<?php
$arg = array('category_name'=>'image-study');
$custom_post = new WP_Query($arg);
?>

<?php while($custom_post->have_posts()): ?>
<?php $custom_post->the_post(); ?>

<section class="item">
<a href="#">
<h4><?php the_title(); ?></h4>
<?php the_content(); ?>
</a>
</section>
<?php endwhile; ?>


</div><!-- ./flex-box -->
</section><!-- /.study -->

</div><!-- /.contents-wrapper -->
</section><!-- /.image -->




<!-- --Other--------------------------------------------- -->
<section class="contents other">
<h2 id="other">Other</h2>

<div class="contents-wrapper">

<p>フェリカに入学する前に自主的に作成した制作物などをまとめました。</p>

<div class="flex-box original-box">

<!-- 表示する投稿記事の種類を限定する -->
<?php
$arg = array('category_name'=>'other');
$custom_post = new WP_Query($arg);
?>

<?php while($custom_post->have_posts()): ?>
<?php $custom_post->the_post(); ?>

<section class="item">
<a href="#">
<h4><?php the_title(); ?></h4>
<?php the_content(); ?>
</a>
</section>
<?php endwhile; ?>


</div><!--  /.flex-box -->
</div><!-- /.contents-wrapper -->

</section><!-- /.oter -->
</main>


<a href="#" class="top">top</a>

<!-- --footer--------------------------------------------- -->
<footer class="footer">
<p><small>2022年 Portfolio Site</small></p>
</footer>

<script>
  const hamburger = document.querySelector('.hamburger');
    hamburger.addEventListener("touchstart", function() {
    hamburger.classList.toggle("is-active");
    document.querySelector('.g-nav').classList.toggle("open");
  });

</script>
</body>
</html>
