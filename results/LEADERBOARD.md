# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 18, 1:20 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 693 windows, 19180 settled trades, 38 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 368 | 34.0 | 34.9 | $-262.42 | -7.1% | $737.58 | -1.0 | done | can't tell from luck |
| momentum_60m_0.30pct | 1618 | 50.4 | 49.5 | $-439.72 | -2.7% | $560.28 | -1.1 | done | can't tell from luck |
| value_ev10 | 889 | 38.2 | 39.1 | $-541.31 | -6.1% | $458.69 | -1.5 | done | can't tell from luck |
| trend_filter | 1118 | 50.4 | 50.9 | $-582.75 | -5.2% | $417.25 | -1.8 | done | can't tell from luck |
| value_ev5 | 1337 | 40.8 | 41.1 | $-606.53 | -4.5% | $393.47 | -1.4 | done | can't tell from luck |
| reversal_15m_0.10pct | 1967 | 51.3 | 50.8 | $-627.74 | -3.2% | $372.26 | -1.4 | done | can't tell from luck |
| coinflip | 2766 | 50.0 | 50.2 | $-1250.37 | -4.5% | $-250.37 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 1618 | 49.6 | 51.3 | $-1260.59 | -7.8% | $-260.59 | -3.2 | done | losing for real |
| momentum_15m_0.10pct | 1967 | 48.7 | 50.0 | $-1281.31 | -6.5% | $-281.31 | -2.9 | done | losing for real |
| momentum_5m_0.00pct | 2766 | 50.8 | 51.8 | $-1515.86 | -5.5% | $-515.86 | -3.0 | done | losing for real |
| always_up | 2766 | 47.4 | 49.5 | $-2343.69 | -8.5% | $-1343.69 | -4.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4348 | 48.2 | 49.1 | $-2533.07 |
| ETH | 4773 | 48.2 | 48.5 | $-2810.31 |
| SOL | 5006 | 48.1 | 48.6 | $-2913.72 |
| XRP | 5053 | 48.5 | 48.3 | $-2455.19 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
