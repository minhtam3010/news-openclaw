from dotenv import load_dotenv

load_dotenv()


from api.news import fetchNewsContent
from llm.groq import callLLM


def main():
    print(
        callLLM(
            """
    Lửa bùng lên dữ dội cùng nhiều tiếng nổ lớn, cột khói bốc cao hàng trăm mét ở khu công nghiệp Nhơn Trạch 6, trưa 10/5.
Khoảng 11h30, lửa bùng lên tại khu sản xuất của Công ty TNHH Uniwin Việt Nam, chuyên dệt may, trong KCN Nhơn Trạch 6, xã Phước An. Bảo vệ và nhân viên dùng hệ thống chữa cháy tại chỗ dập lửa nhưng không thành.
Do nguyên vật liệu chủ yếu là vải cùng nhiều thiết bị ngành dệt, đám cháy nhanh chóng lan rộng ra khu nhà xưởng rộng hàng nghìn m2. Cột khói bốc cao hàng trăm mét, từ xa nhiều km vẫn có thể nhìn thấy.
Theo nhân chứng, lửa bùng dữ dội kèm nhiều tiếng nổ lớn nên không ai dám tiếp cận gần. Một số container gần đám cháy cũng không thể di chuyển ra ngoài. Các công ty lân cận phải phun nước làm mát để ngăn cháy lan.
Công an TP Đồng Nai đang điều động nhiều xe chuyên dụng cùng lực lượng chữa cháy tiếp cận hiện trường.
Hai ngày trước, một công ty dệt may khác trong KCN Nhơn Trạch 5, gần KCN Nhơn Trạch 6, cũng xảy ra hỏa hoạn vào buổi tối, thiêu rụi nhiều tài sản, máy móc và nhà xưởng.
    """
        )
    )


if __name__ == "__main__":
    main()
