# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 24, 5:20 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1333 windows, 35155 settled trades, 418 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 693 | 34.3 | 35.4 | $-518.07 | -7.5% | $481.93 | -1.5 | done | can't tell from luck |
| value_ev10 | 1694 | 38.8 | 39.2 | $-800.05 | -4.7% | $199.95 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 3521 | 50.9 | 50.2 | $-1015.11 | -2.9% | $-15.11 | -1.7 | done | can't tell from luck |
| value_ev5 | 2557 | 40.5 | 41.1 | $-1293.07 | -5.1% | $-293.07 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 2954 | 49.4 | 49.5 | $-1442.55 | -4.9% | $-442.55 | -2.6 | done | losing for real |
| reversal_60m_0.30pct | 2954 | 50.6 | 50.9 | $-1549.60 | -5.2% | $-549.60 | -2.9 | done | losing for real |
| trend_filter | 2093 | 48.7 | 50.5 | $-1782.68 | -8.5% | $-782.68 | -4.0 | done | losing for real |
| momentum_15m_0.10pct | 3521 | 49.1 | 50.2 | $-2227.16 | -6.3% | $-1227.16 | -3.8 | done | losing for real |
| coinflip | 5056 | 49.9 | 50.1 | $-2351.97 | -4.7% | $-1351.97 | -3.3 | done | losing for real |
| momentum_5m_0.00pct | 5056 | 50.3 | 51.4 | $-3016.37 | -6.0% | $-2016.37 | -4.4 | done | losing for real |
| always_up | 5056 | 47.9 | 49.3 | $-3659.97 | -7.2% | $-2659.97 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 8588 | 47.9 | 48.9 | $-5226.96 |
| ETH | 9257 | 48.2 | 48.2 | $-4845.43 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
