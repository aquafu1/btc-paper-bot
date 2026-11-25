# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 25, 3:00 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1372 windows, 35680 settled trades, 435 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 710 | 34.1 | 35.3 | $-579.64 | -8.2% | $420.36 | -1.7 | done | can't tell from luck |
| value_ev10 | 1729 | 38.7 | 39.2 | $-828.68 | -4.8% | $171.32 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 3566 | 50.8 | 50.1 | $-1023.45 | -2.9% | $-23.45 | -1.7 | done | can't tell from luck |
| value_ev5 | 2605 | 40.4 | 41.1 | $-1320.78 | -5.1% | $-320.78 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 2991 | 49.2 | 49.4 | $-1505.42 | -5.0% | $-505.42 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 2991 | 50.8 | 50.9 | $-1514.00 | -5.1% | $-514.00 | -2.8 | done | losing for real |
| trend_filter | 2120 | 48.5 | 50.4 | $-1873.46 | -8.8% | $-873.46 | -4.2 | done | losing for real |
| coinflip | 5134 | 50.1 | 50.0 | $-2196.61 | -4.3% | $-1196.61 | -3.1 | done | losing for real |
| momentum_15m_0.10pct | 3566 | 49.2 | 50.2 | $-2213.66 | -6.2% | $-1213.66 | -3.7 | done | losing for real |
| momentum_5m_0.00pct | 5134 | 50.1 | 51.3 | $-3206.10 | -6.2% | $-2206.10 | -4.6 | done | losing for real |
| always_up | 5134 | 47.9 | 49.3 | $-3699.60 | -7.2% | $-2699.60 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 8843 | 47.9 | 48.8 | $-5193.99 |
| ETH | 9527 | 48.1 | 48.1 | $-5183.16 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
