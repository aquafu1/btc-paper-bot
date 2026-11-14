# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 14, 6:50 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 331 windows, 8825 settled trades, 44 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 704 | 53.4 | 51.7 | $-64.84 | -0.9% | $935.16 | -0.3 | done | can't tell from luck |
| value_ev20 | 175 | 36.0 | 36.6 | $-103.62 | -5.9% | $896.38 | -0.6 | Sat 7:00 PM | too few trades (175/200) |
| reversal_15m_0.10pct | 874 | 53.0 | 52.0 | $-199.47 | -2.3% | $800.53 | -0.7 | done | can't tell from luck |
| value_ev10 | 429 | 38.7 | 40.3 | $-333.92 | -7.8% | $666.08 | -1.4 | done | can't tell from luck |
| value_ev5 | 637 | 40.3 | 42.0 | $-505.42 | -7.9% | $494.58 | -1.7 | done | can't tell from luck |
| coinflip | 1316 | 50.1 | 50.9 | $-734.76 | -5.6% | $265.24 | -2.1 | done | losing for real |
| trend_filter | 480 | 44.8 | 50.3 | $-743.78 | -15.5% | $256.22 | -3.5 | done | losing for real |
| momentum_60m_0.30pct | 704 | 46.6 | 49.9 | $-802.38 | -11.4% | $197.62 | -3.1 | done | losing for real |
| momentum_15m_0.10pct | 874 | 47.0 | 49.8 | $-849.69 | -9.7% | $150.31 | -2.9 | done | losing for real |
| always_up | 1316 | 47.9 | 50.3 | $-1159.62 | -8.8% | $-159.62 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 1316 | 48.3 | 51.3 | $-1263.31 | -9.6% | $-263.31 | -3.6 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1970 | 46.6 | 49.3 | $-1827.89 |
| ETH | 2214 | 47.2 | 48.7 | $-1869.27 |
| SOL | 2301 | 47.8 | 49.2 | $-1826.83 |
| XRP | 2340 | 48.7 | 49.0 | $-1236.83 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
