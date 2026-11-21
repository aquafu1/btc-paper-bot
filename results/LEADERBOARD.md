# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 8:00 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 960 windows, 26592 settled trades, 46 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 488 | 35.2 | 34.9 | $-139.50 | -2.9% | $860.50 | -0.5 | done | can't tell from luck |
| value_ev10 | 1208 | 38.3 | 39.1 | $-602.30 | -5.0% | $397.70 | -1.4 | done | can't tell from luck |
| reversal_15m_0.10pct | 2717 | 51.4 | 50.6 | $-667.91 | -2.5% | $332.09 | -1.3 | done | can't tell from luck |
| momentum_60m_0.30pct | 2270 | 50.1 | 49.7 | $-901.20 | -4.0% | $98.80 | -1.9 | done | can't tell from luck |
| value_ev5 | 1835 | 40.1 | 41.0 | $-953.13 | -5.2% | $46.87 | -1.9 | done | can't tell from luck |
| trend_filter | 1591 | 49.8 | 50.9 | $-1075.59 | -6.8% | $-75.59 | -2.8 | done | losing for real |
| reversal_60m_0.30pct | 2270 | 49.9 | 51.0 | $-1578.09 | -7.0% | $-578.09 | -3.4 | done | losing for real |
| coinflip | 3832 | 50.1 | 50.4 | $-1782.28 | -4.7% | $-782.28 | -2.9 | done | losing for real |
| momentum_15m_0.10pct | 2717 | 48.6 | 50.3 | $-1947.84 | -7.2% | $-947.84 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 3832 | 50.8 | 51.5 | $-2036.61 | -5.3% | $-1036.61 | -3.4 | done | losing for real |
| always_up | 3832 | 46.9 | 49.6 | $-3749.33 | -9.8% | $-2749.33 | -6.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6059 | 48.1 | 49.0 | $-3482.10 |
| ETH | 6604 | 48.1 | 48.5 | $-4008.73 |
| SOL | 6944 | 48.3 | 48.6 | $-3744.19 |
| XRP | 6985 | 48.2 | 48.5 | $-4198.77 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
