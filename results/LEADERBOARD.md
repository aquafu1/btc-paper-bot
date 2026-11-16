# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 16, 8:05 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 528 windows, 14586 settled trades, 36 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1244 | 51.6 | 49.9 | $-89.83 | -0.7% | $910.17 | -0.3 | done | can't tell from luck |
| value_ev20 | 277 | 35.0 | 35.5 | $-182.64 | -6.6% | $817.36 | -0.8 | done | can't tell from luck |
| value_ev10 | 681 | 38.2 | 39.7 | $-525.95 | -7.7% | $474.05 | -1.7 | done | can't tell from luck |
| momentum_15m_0.10pct | 1479 | 50.0 | 49.7 | $-536.68 | -3.6% | $463.32 | -1.4 | done | can't tell from luck |
| trend_filter | 855 | 49.7 | 50.8 | $-540.09 | -6.3% | $459.91 | -1.9 | done | can't tell from luck |
| value_ev5 | 1015 | 40.3 | 41.5 | $-679.58 | -6.7% | $320.42 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 1479 | 50.0 | 51.4 | $-1044.86 | -7.1% | $-44.86 | -2.8 | done | losing for real |
| coinflip | 2104 | 49.8 | 50.6 | $-1185.52 | -5.6% | $-185.52 | -2.6 | done | losing for real |
| reversal_60m_0.30pct | 1244 | 48.4 | 51.2 | $-1243.22 | -10.0% | $-243.22 | -3.6 | done | losing for real |
| momentum_5m_0.00pct | 2104 | 49.3 | 51.6 | $-1733.98 | -8.2% | $-733.98 | -3.9 | done | losing for real |
| always_up | 2104 | 46.5 | 50.1 | $-2405.08 | -11.4% | $-1405.08 | -5.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3302 | 47.4 | 49.2 | $-2648.97 |
| ETH | 3636 | 47.9 | 48.7 | $-2434.09 |
| SOL | 3805 | 47.6 | 48.9 | $-2816.15 |
| XRP | 3843 | 48.3 | 48.8 | $-2268.21 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
