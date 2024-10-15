-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 15, 2024 at 04:46 PM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.1.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `e_lance`
--

-- --------------------------------------------------------

--
-- Table structure for table `addresses`
--

CREATE TABLE `addresses` (
  `address_id` int(10) NOT NULL,
  `user_id` int(10) DEFAULT NULL,
  `zipcode` int(10) NOT NULL,
  `other_detail` varchar(10) DEFAULT NULL,
  `brgy_address` varchar(255) NOT NULL,
  `municipality` varchar(255) NOT NULL,
  `city` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `categories`
--

CREATE TABLE `categories` (
  `category_id` int(10) NOT NULL,
  `user_id` int(10) DEFAULT NULL,
  `category_name` varchar(255) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` datetime DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `status` int(1) DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `categories`
--

INSERT INTO `categories` (`category_id`, `user_id`, `category_name`, `created_at`, `updated_at`, `status`) VALUES
(1, 4, 'Clothes', '2024-10-11 09:04:19', NULL, 1),
(2, 10, 'Electronics', '2024-10-11 10:29:22', '2024-10-11 21:50:07', 1),
(3, 4, 'Furniture', '2024-10-11 10:30:09', '2024-10-11 21:50:09', 1),
(4, 4, 'Appliances', '2024-10-11 12:04:33', NULL, 1),
(5, 4, 'Shoes', '2024-10-11 12:20:34', '2024-10-11 20:20:34', 1),
(6, 4, 'Appliances 2', '2024-10-11 12:58:56', '2024-10-15 20:24:56', 1),
(7, 4, 'Candy', '2024-10-11 13:01:48', '2024-10-11 21:01:48', 1),
(8, 4, 'toys', '2024-10-11 13:06:14', '2024-10-11 22:42:29', 2),
(9, 4, 'foods', '2024-10-11 13:06:49', '2024-10-11 21:51:23', 2),
(10, 4, 'foods 1', '2024-10-11 13:10:29', '2024-10-11 21:51:16', 2),
(11, 4, 'xxx', '2024-10-12 10:29:13', '2024-10-12 18:29:18', 2),
(12, 4, 'sasddsa', '2024-10-12 10:29:39', '2024-10-12 18:29:48', 2),
(13, 4, 'asddas', '2024-10-12 10:30:31', '2024-10-12 20:38:54', 2),
(14, 4, 'Noodles', '2024-10-12 10:42:37', '2024-10-12 18:54:14', 1),
(15, 4, 'gasgas', '2024-10-12 10:52:37', '2024-10-12 20:41:50', 2),
(16, 4, 'axsaxsa', '2024-10-13 08:09:54', '2024-10-13 16:10:10', 2),
(17, 4, 'Test', '2024-10-13 19:10:36', '2024-10-14 03:10:42', 2),
(18, 4, 'Fashion', '2024-10-14 12:32:38', '2024-10-14 20:32:38', 1),
(19, 4, 'Fashion 1', '2024-10-14 12:32:56', '2024-10-14 20:33:06', NULL),
(20, 4, 'jshjas', '2024-10-14 12:34:12', '2024-10-14 20:34:18', NULL),
(21, 4, 'dsa', '2024-10-14 12:37:07', '2024-10-14 20:37:21', NULL),
(22, 4, 'saddas', '2024-10-14 12:43:58', '2024-10-14 20:44:04', 2),
(23, 4, 'ds', '2024-10-14 13:06:34', '2024-10-14 21:06:39', 2);

-- --------------------------------------------------------

--
-- Table structure for table `orders`
--

CREATE TABLE `orders` (
  `order_id` int(10) NOT NULL,
  `product_id` int(10) DEFAULT NULL,
  `user_id` int(10) DEFAULT NULL,
  `order_name` varchar(255) DEFAULT NULL,
  `reference` int(20) DEFAULT NULL,
  `total_amount` int(10) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` datetime DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `status` int(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `order_items`
--

CREATE TABLE `order_items` (
  `order_items_id` int(10) NOT NULL,
  `product_id` int(10) DEFAULT NULL,
  `reference` int(20) DEFAULT NULL,
  `status` int(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `payments`
--

CREATE TABLE `payments` (
  `payment_id` int(10) NOT NULL,
  `order_id` int(10) DEFAULT NULL,
  `payment_method_id` int(10) DEFAULT NULL,
  `payment_date` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `payment_amount` int(10) DEFAULT NULL,
  `status` int(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `payment_methods`
--

CREATE TABLE `payment_methods` (
  `payment_method_id` int(10) NOT NULL,
  `payment_name` varchar(255) DEFAULT NULL,
  `status` int(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `products`
--

CREATE TABLE `products` (
  `product_id` int(10) NOT NULL,
  `category_id` int(10) DEFAULT NULL,
  `product_name` varchar(255) DEFAULT NULL,
  `description` longtext DEFAULT NULL,
  `price` int(10) DEFAULT NULL,
  `sale_percent` int(10) DEFAULT 0,
  `qty` int(10) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` datetime DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `status` int(1) DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `products`
--

INSERT INTO `products` (`product_id`, `category_id`, `product_name`, `description`, `price`, `sale_percent`, `qty`, `created_at`, `updated_at`, `status`) VALUES
(51, 5, 'Jordan', 'sddd', 44, 0, 43, '2024-10-13 18:18:19', '2024-10-14 02:18:19', 1),
(52, 4, 'Refrigirator', 'dadas', 12000, 0, 34, '2024-10-13 19:19:36', '2024-10-14 03:19:36', 1),
(53, 14, 'Extra Big', '<p><span style=\"background-color: rgb(255, 255, 255); color: rgb(51, 65, 85);\">If you’re a fan of mysteries, detective stories, or challenging puzzles, the&nbsp;</span><strong style=\"background-color: rgb(255, 255, 255); color: rgb(51, 65, 85);\">Sherlock vs Illuminati</strong><span style=\"background-color: rgb(255, 255, 255); color: rgb(51, 65, 85);\">&nbsp;escape room at&nbsp;</span><strong style=\"background-color: rgb(255, 255, 255); color: rgb(51, 65, 85);\">Escape in Time Spring</strong><span style=\"background-color: rgb(255, 255, 255); color: rgb(51, 65, 85);\">&nbsp;is the adventure you’ve been waiting for. This thrilling experience puts you in the shoes of Sherlock Holmes, the world’s greatest detective, as you take on the shadowy Illuminati. Can you crack the case before time runs out?</span></p><h3><span style=\"background-color: rgb(255, 255, 255); color: var(--ast-global-color-2);\">The Story: A Conspiracy Unfolds</span></h3><p><span style=\"background-color: rgb(255, 255, 255); color: rgb(51, 65, 85);\">The plot of&nbsp;</span><strong style=\"background-color: rgb(255, 255, 255); color: rgb(51, 65, 85);\">Sherlock vs Illuminati</strong><span style=\"background-color: rgb(255, 255, 255); color: rgb(51, 65, 85);\">&nbsp;sets the stage for a mind-bending mystery. Sherlock Holmes has uncovered evidence that suggests the Illuminati—a secret organization bent on controlling global events—has been manipulating history from the shadows. As you and your team step into Sherlock’s shoes, your mission is to gather clues, decipher codes, and unravel the mystery behind the Illuminati’s influence before they strike again.</span></p><p><span style=\"background-color: rgb(255, 255, 255); color: rgb(51, 65, 85);\">But it’s not going to be easy. The Illuminati have gone to great lengths to cover their tracks, and they know Sherlock is on to them. You’ll have to outsmart their traps and think like the master detective himself to solve this case.</span></p><h3><span style=\"background-color: rgb(255, 255, 255); color: var(--ast-global-color-2);\">The Challenge: Puzzle-Solving and Deduction</span></h3><p><strong style=\"background-color: rgb(255, 255, 255); color: rgb(51, 65, 85);\">Sherlock vs Illuminati</strong><span style=\"background-color: rgb(255, 255, 255); color: rgb(51, 65, 85);\">&nbsp;is more than just an escape room—it’s an intellectual battle. The room is packed with challenging puzzles that require a sharp mind, teamwork, and keen attention to detail. You’ll encounter cryptic messages, hidden clues, and intricate locks that test your problem-solving abilities.</span></p><p><span style=\"background-color: rgb(255, 255, 255); color: rgb(51, 65, 85);\">Each puzzle is designed to push your limits, and there’s no room for error. The combination of logic, observation, and teamwork is crucial to your success. Every solved riddle brings you closer to exposing the Illuminati’s secret plan, but the clock is ticking, and time is not on your side.</span></p><p><span style=\"background-color: rgb(255, 255, 255); color: rgb(51, 65, 85);\">Key skills you’ll need:</span></p><ol><li data-list=\"bullet\"><span class=\"ql-ui\" contenteditable=\"false\"></span><strong style=\"background-color: rgb(255, 255, 255); color: rgb(51, 65, 85);\">Deductive reasoning</strong><span style=\"background-color: rgb(255, 255, 255); color: rgb(51, 65, 85);\">: Just like Sherlock, you’ll need to think logically and make connections between seemingly unrelated clues.</span></li><li data-list=\"bullet\"><span class=\"ql-ui\" contenteditable=\"false\"></span><strong style=\"background-color: rgb(255, 255, 255); color: rgb(51, 65, 85);\">Teamwork</strong><span style=\"background-color: rgb(255, 255, 255); color: rgb(51, 65, 85);\">: Collaboration is essential, as the puzzles require different perspectives and skills to solve.</span></li><li data-list=\"bullet\"><span class=\"ql-ui\" contenteditable=\"false\"></span><strong style=\"background-color: rgb(255, 255, 255); color: rgb(51, 65, 85);\">Attention to detail</strong><span style=\"background-color: rgb(255, 255, 255); color: rgb(51, 65, 85);\">: No clue is too small, and often the most overlooked details hold the key to unlocking the next phase of your mission.</span></li></ol><h3><span style=\"background-color: rgb(255, 255, 255); color: var(--ast-global-color-2);\">The Atmosphere: Immersive and Intense</span></h3><p><span style=\"background-color: rgb(255, 255, 255); color: rgb(51, 65, 85);\">One of the highlights of the&nbsp;</span><strong style=\"background-color: rgb(255, 255, 255); color: rgb(51, 65, 85);\">Sherlock vs Illuminati</strong><span style=\"background-color: rgb(255, 255, 255); color: rgb(51, 65, 85);\">&nbsp;escape room is its immersive atmosphere. The room is intricately designed to transport you into Sherlock’s world—complete with Victorian-era decor and the shadowy, secretive vibe of the Illuminati. The moment you step inside, you’ll feel as though you’ve been transported into a classic Sherlock Holmes adventure, where danger lurks around every corner and the stakes are incredibly high.</span></p><p><br></p>', 12, 0, 22, '2024-10-14 12:03:22', '2024-10-14 20:03:22', 1),
(54, 5, 'panget mo', '<p>sffwsds</p>', 1212, 0, 2, '2024-10-14 12:52:49', '2024-10-14 21:01:52', 2),
(55, 18, 'dd', '<p>das</p>', 321, 0, 2, '2024-10-14 13:08:02', '2024-10-14 21:08:08', 2);

-- --------------------------------------------------------

--
-- Table structure for table `product_attachments`
--

CREATE TABLE `product_attachments` (
  `product_attachment_id` int(10) NOT NULL,
  `product_id` int(10) DEFAULT NULL,
  `attachment` varchar(255) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` datetime DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `status` int(1) DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `product_attachments`
--

INSERT INTO `product_attachments` (`product_attachment_id`, `product_id`, `attachment`, `created_at`, `updated_at`, `status`) VALUES
(1, 51, '289189075993562.png', '2024-10-13 18:18:19', '2024-10-14 02:18:19', 1),
(2, 51, '494148786499683.png', '2024-10-13 18:18:19', '2024-10-14 02:18:19', 1),
(3, 52, '659890926928580.png', '2024-10-13 19:19:36', '2024-10-14 03:19:36', 1),
(4, 52, '846653235332768.jpeg', '2024-10-13 19:19:36', '2024-10-14 03:19:36', 1),
(5, 53, '651439242035307.png', '2024-10-14 12:03:22', '2024-10-14 20:03:22', 1),
(6, 53, '703754199822529.png', '2024-10-14 12:03:22', '2024-10-14 20:03:22', 1),
(7, 54, '521298041327190.png', '2024-10-14 12:52:49', '2024-10-14 20:52:49', 1),
(8, 54, '848110163043614.png', '2024-10-14 12:52:49', '2024-10-14 20:52:49', 1),
(9, 55, '608564591158806.png', '2024-10-14 13:08:02', '2024-10-14 21:08:02', 1);

-- --------------------------------------------------------

--
-- Table structure for table `roles`
--

CREATE TABLE `roles` (
  `role_id` int(10) NOT NULL,
  `name` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `roles`
--

INSERT INTO `roles` (`role_id`, `name`) VALUES
(1, 'Admin'),
(2, 'Buyer'),
(3, 'Buyer/Seller');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `user_id` int(10) NOT NULL,
  `role_id` int(10) DEFAULT 2,
  `firstname` varchar(255) DEFAULT NULL,
  `lastname` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `phone` varchar(11) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` datetime DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `status` int(1) DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`user_id`, `role_id`, `firstname`, `lastname`, `email`, `password`, `phone`, `created_at`, `updated_at`, `status`) VALUES
(1, 1, 'Lawrence', 'Celis', 'oyencelis@gmail.com', '962314b7ef2f70007380c5b6700daedc6343ac6938e8241a44713e721993c0ac', '09852074296', '2024-10-08 12:25:25', NULL, 1),
(4, 3, 'law', 'pogi', 'law123@gmail.com', '8d2d29599895ac3b66d2a4a244cefc05a0fe91b4dd9f91c600c1e3e2759766cc', '09251726253', '2024-10-11 09:00:18', NULL, 1),
(10, 2, 'leri', 'leri', 'leri@gmail.com', 'a37c5e93676834c145593ddf79da212f0c2fc98efd582b1a9fcf64ce20097cec', '12345678991', '2024-10-10 01:37:51', NULL, 1);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `addresses`
--
ALTER TABLE `addresses`
  ADD PRIMARY KEY (`address_id`),
  ADD KEY `FK_address` (`user_id`);

--
-- Indexes for table `categories`
--
ALTER TABLE `categories`
  ADD PRIMARY KEY (`category_id`),
  ADD KEY `FK_categories` (`user_id`);

--
-- Indexes for table `orders`
--
ALTER TABLE `orders`
  ADD PRIMARY KEY (`order_id`),
  ADD KEY `FK_orders` (`product_id`),
  ADD KEY `FK_orders_user_id` (`user_id`);

--
-- Indexes for table `order_items`
--
ALTER TABLE `order_items`
  ADD PRIMARY KEY (`order_items_id`),
  ADD KEY `FK_order_items` (`product_id`);

--
-- Indexes for table `payments`
--
ALTER TABLE `payments`
  ADD PRIMARY KEY (`payment_id`),
  ADD KEY `FK_payments` (`order_id`),
  ADD KEY `FK_payments_method` (`payment_method_id`);

--
-- Indexes for table `payment_methods`
--
ALTER TABLE `payment_methods`
  ADD PRIMARY KEY (`payment_method_id`);

--
-- Indexes for table `products`
--
ALTER TABLE `products`
  ADD PRIMARY KEY (`product_id`),
  ADD KEY `FK_products` (`category_id`);

--
-- Indexes for table `product_attachments`
--
ALTER TABLE `product_attachments`
  ADD PRIMARY KEY (`product_attachment_id`),
  ADD KEY `FK_product_attachments` (`product_id`);

--
-- Indexes for table `roles`
--
ALTER TABLE `roles`
  ADD PRIMARY KEY (`role_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`user_id`),
  ADD KEY `FK_users` (`role_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `addresses`
--
ALTER TABLE `addresses`
  MODIFY `address_id` int(10) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `categories`
--
ALTER TABLE `categories`
  MODIFY `category_id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- AUTO_INCREMENT for table `orders`
--
ALTER TABLE `orders`
  MODIFY `order_id` int(10) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `order_items`
--
ALTER TABLE `order_items`
  MODIFY `order_items_id` int(10) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `payments`
--
ALTER TABLE `payments`
  MODIFY `payment_id` int(10) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `payment_methods`
--
ALTER TABLE `payment_methods`
  MODIFY `payment_method_id` int(10) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `products`
--
ALTER TABLE `products`
  MODIFY `product_id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=56;

--
-- AUTO_INCREMENT for table `product_attachments`
--
ALTER TABLE `product_attachments`
  MODIFY `product_attachment_id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `roles`
--
ALTER TABLE `roles`
  MODIFY `role_id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `user_id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `addresses`
--
ALTER TABLE `addresses`
  ADD CONSTRAINT `FK_address` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`);

--
-- Constraints for table `categories`
--
ALTER TABLE `categories`
  ADD CONSTRAINT `FK_categories` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`);

--
-- Constraints for table `orders`
--
ALTER TABLE `orders`
  ADD CONSTRAINT `FK_orders` FOREIGN KEY (`product_id`) REFERENCES `products` (`product_id`),
  ADD CONSTRAINT `FK_orders_user_id` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`);

--
-- Constraints for table `order_items`
--
ALTER TABLE `order_items`
  ADD CONSTRAINT `FK_order_items` FOREIGN KEY (`product_id`) REFERENCES `products` (`product_id`);

--
-- Constraints for table `payments`
--
ALTER TABLE `payments`
  ADD CONSTRAINT `FK_payments` FOREIGN KEY (`order_id`) REFERENCES `orders` (`order_id`),
  ADD CONSTRAINT `FK_payments_method` FOREIGN KEY (`payment_method_id`) REFERENCES `payment_methods` (`payment_method_id`);

--
-- Constraints for table `products`
--
ALTER TABLE `products`
  ADD CONSTRAINT `FK_products` FOREIGN KEY (`category_id`) REFERENCES `categories` (`category_id`);

--
-- Constraints for table `product_attachments`
--
ALTER TABLE `product_attachments`
  ADD CONSTRAINT `FK_product_attachments` FOREIGN KEY (`product_id`) REFERENCES `products` (`product_id`);

--
-- Constraints for table `users`
--
ALTER TABLE `users`
  ADD CONSTRAINT `FK_users` FOREIGN KEY (`role_id`) REFERENCES `roles` (`role_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
