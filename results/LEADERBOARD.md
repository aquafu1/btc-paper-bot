# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 14, 5:20 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 325 windows, 8690 settled trades, 33 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 701 | 53.4 | 51.8 | $-81.14 | -1.2% | $918.86 | -0.3 | done | can't tell from luck |
| reversal_15m_0.10pct | 864 | 53.0 | 52.0 | $-195.60 | -2.3% | $804.40 | -0.7 | done | can't tell from luck |
| value_ev20 | 165 | 33.3 | 36.7 | $-232.09 | -14.1% | $767.91 | -1.4 | Sat 11:15 PM | too few trades (165/200) |
| value_ev10 | 417 | 37.4 | 40.4 | $-489.41 | -11.7% | $510.59 | -2.1 | done | losing for real |
| value_ev5 | 624 | 39.4 | 42.2 | $-675.19 | -10.8% | $324.81 | -2.4 | done | losing for real |
| trend_filter | 478 | 44.8 | 50.3 | $-738.15 | -15.4% | $261.85 | -3.5 | done | losing for real |
| coinflip | 1292 | 50.2 | 51.0 | $-755.35 | -5.8% | $244.65 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 701 | 46.6 | 49.9 | $-786.76 | -11.2% | $213.24 | -3.0 | done | losing for real |
| momentum_15m_0.10pct | 864 | 47.0 | 49.8 | $-846.98 | -9.8% | $153.02 | -2.9 | done | losing for real |
| always_up | 1292 | 47.8 | 50.4 | $-1210.62 | -9.4% | $-210.62 | -3.4 | done | losing for real |
| momentum_5m_0.00pct | 1292 | 48.1 | 51.3 | $-1341.36 | -10.4% | $-341.36 | -3.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1944 | 46.4 | 49.3 | $-1966.31 |
| ETH | 2182 | 46.7 | 48.8 | $-2190.85 |
| SOL | 2262 | 47.9 | 49.3 | $-1857.29 |
| XRP | 2302 | 48.6 | 49.1 | $-1338.19 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
