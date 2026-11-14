# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 14, 5:35 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 326 windows, 8709 settled trades, 35 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 701 | 53.4 | 51.8 | $-81.14 | -1.2% | $918.86 | -0.3 | done | can't tell from luck |
| reversal_15m_0.10pct | 867 | 52.9 | 52.0 | $-209.09 | -2.4% | $790.91 | -0.7 | done | can't tell from luck |
| value_ev20 | 165 | 33.3 | 36.7 | $-232.09 | -14.1% | $767.91 | -1.4 | Sat 11:30 PM | too few trades (165/200) |
| value_ev10 | 417 | 37.4 | 40.4 | $-489.41 | -11.7% | $510.59 | -2.1 | done | losing for real |
| value_ev5 | 624 | 39.4 | 42.2 | $-675.19 | -10.8% | $324.81 | -2.4 | done | losing for real |
| trend_filter | 479 | 44.7 | 50.3 | $-748.15 | -15.6% | $251.85 | -3.5 | done | losing for real |
| coinflip | 1296 | 50.2 | 51.0 | $-757.35 | -5.8% | $242.65 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 701 | 46.6 | 49.9 | $-786.76 | -11.2% | $213.24 | -3.0 | done | losing for real |
| momentum_15m_0.10pct | 867 | 47.1 | 49.8 | $-838.98 | -9.7% | $161.02 | -2.9 | done | losing for real |
| always_up | 1296 | 47.8 | 50.4 | $-1234.11 | -9.5% | $-234.11 | -3.5 | done | losing for real |
| momentum_5m_0.00pct | 1296 | 48.1 | 51.3 | $-1364.62 | -10.5% | $-364.62 | -4.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1947 | 46.4 | 49.3 | $-1979.58 |
| ETH | 2187 | 46.7 | 48.8 | $-2205.00 |
| SOL | 2268 | 47.9 | 49.3 | $-1884.27 |
| XRP | 2307 | 48.6 | 49.1 | $-1348.04 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
