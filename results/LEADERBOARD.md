# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 4:00 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 944 windows, 26129 settled trades, 74 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 482 | 35.1 | 34.9 | $-163.29 | -3.4% | $836.71 | -0.6 | done | can't tell from luck |
| value_ev10 | 1185 | 38.1 | 39.1 | $-681.30 | -5.7% | $318.70 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 2671 | 51.0 | 50.6 | $-897.48 | -3.4% | $102.52 | -1.7 | done | can't tell from luck |
| momentum_60m_0.30pct | 2233 | 50.1 | 49.8 | $-971.05 | -4.3% | $28.95 | -2.1 | done | losing for real |
| trend_filter | 1552 | 49.9 | 51.0 | $-1088.47 | -7.0% | $-88.47 | -2.8 | done | losing for real |
| value_ev5 | 1798 | 39.8 | 41.0 | $-1108.52 | -6.2% | $-108.52 | -2.2 | done | losing for real |
| reversal_60m_0.30pct | 2233 | 49.9 | 50.9 | $-1552.49 | -7.0% | $-552.49 | -3.4 | done | losing for real |
| coinflip | 3768 | 50.4 | 50.3 | $-1591.28 | -4.2% | $-591.28 | -2.6 | done | losing for real |
| momentum_15m_0.10pct | 2671 | 49.0 | 50.3 | $-1739.88 | -6.5% | $-739.88 | -3.4 | done | losing for real |
| momentum_5m_0.00pct | 3768 | 51.0 | 51.6 | $-1931.68 | -5.1% | $-931.68 | -3.3 | done | losing for real |
| always_up | 3768 | 46.8 | 49.7 | $-3834.33 | -10.2% | $-2834.33 | -6.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5957 | 48.2 | 49.1 | $-3400.06 |
| ETH | 6499 | 48.1 | 48.6 | $-4116.13 |
| SOL | 6814 | 48.2 | 48.6 | $-4006.63 |
| XRP | 6859 | 48.3 | 48.5 | $-4036.97 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
