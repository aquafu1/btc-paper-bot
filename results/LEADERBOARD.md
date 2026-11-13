# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 13, 4:20 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 273 windows, 7165 settled trades, 74 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 704 | 54.5 | 52.3 | $+15.40 | +0.2% | $1015.40 | +0.1 | done | can't tell from luck |
| value_ev20 | 129 | 35.7 | 37.0 | $-108.42 | -8.4% | $891.58 | -0.7 | Sun 8:15 AM | too few trades (129/200) |
| reversal_60m_0.30pct | 573 | 52.4 | 52.3 | $-232.99 | -4.1% | $767.01 | -1.0 | done | can't tell from luck |
| value_ev10 | 346 | 38.2 | 40.8 | $-357.16 | -10.3% | $642.84 | -1.6 | done | can't tell from luck |
| trend_filter | 375 | 46.7 | 50.0 | $-429.37 | -11.4% | $570.63 | -2.3 | done | losing for real |
| value_ev5 | 509 | 40.3 | 42.4 | $-471.03 | -9.3% | $528.97 | -1.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 573 | 47.6 | 49.6 | $-509.76 | -8.9% | $490.24 | -2.2 | done | losing for real |
| coinflip | 1084 | 49.5 | 50.9 | $-754.29 | -7.0% | $245.71 | -2.4 | done | losing for real |
| momentum_5m_0.00pct | 1084 | 49.8 | 51.4 | $-782.27 | -7.2% | $217.73 | -2.5 | done | losing for real |
| momentum_15m_0.10pct | 704 | 45.5 | 49.6 | $-872.66 | -12.4% | $127.34 | -3.3 | done | losing for real |
| always_up | 1084 | 47.1 | 50.2 | $-1128.89 | -10.4% | $-128.89 | -3.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1599 | 46.6 | 49.5 | $-1661.90 |
| ETH | 1788 | 46.8 | 49.0 | $-1774.16 |
| SOL | 1856 | 48.4 | 49.3 | $-1323.84 |
| XRP | 1922 | 49.0 | 49.1 | $-871.53 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
