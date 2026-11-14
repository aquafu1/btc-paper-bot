# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 14, 6:20 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 329 windows, 8772 settled trades, 53 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 701 | 53.4 | 51.8 | $-81.14 | -1.2% | $918.86 | -0.3 | done | can't tell from luck |
| value_ev20 | 172 | 35.5 | 36.6 | $-126.85 | -7.4% | $873.15 | -0.8 | Sat 8:15 PM | too few trades (172/200) |
| reversal_15m_0.10pct | 870 | 53.0 | 52.0 | $-206.81 | -2.4% | $793.19 | -0.7 | done | can't tell from luck |
| value_ev10 | 424 | 38.2 | 40.3 | $-384.16 | -9.1% | $615.84 | -1.6 | done | can't tell from luck |
| value_ev5 | 631 | 39.9 | 42.1 | $-569.95 | -9.0% | $430.05 | -2.0 | done | can't tell from luck |
| coinflip | 1308 | 50.1 | 50.9 | $-743.67 | -5.7% | $256.33 | -2.1 | done | losing for real |
| trend_filter | 479 | 44.7 | 50.3 | $-748.15 | -15.6% | $251.85 | -3.5 | done | losing for real |
| momentum_60m_0.30pct | 701 | 46.6 | 49.9 | $-786.76 | -11.2% | $213.24 | -3.0 | done | losing for real |
| momentum_15m_0.10pct | 870 | 47.0 | 49.7 | $-841.67 | -9.7% | $158.33 | -2.9 | done | losing for real |
| always_up | 1308 | 47.9 | 50.3 | $-1141.34 | -8.7% | $-141.34 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 1308 | 48.2 | 51.3 | $-1310.72 | -10.0% | $-310.72 | -3.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1959 | 46.6 | 49.3 | $-1871.41 |
| ETH | 2202 | 47.0 | 48.7 | $-1960.39 |
| SOL | 2287 | 47.7 | 49.3 | $-1924.22 |
| XRP | 2324 | 48.8 | 49.0 | $-1185.21 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
