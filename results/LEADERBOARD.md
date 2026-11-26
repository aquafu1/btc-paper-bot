# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 26, 12:15 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1457 windows, 36875 settled trades, 380 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 748 | 34.1 | 35.3 | $-613.47 | -8.2% | $386.53 | -1.7 | done | can't tell from luck |
| value_ev10 | 1798 | 38.5 | 39.2 | $-926.32 | -5.2% | $73.68 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 3675 | 50.9 | 50.0 | $-989.53 | -2.7% | $10.47 | -1.6 | done | can't tell from luck |
| value_ev5 | 2706 | 40.4 | 41.1 | $-1431.66 | -5.3% | $-431.66 | -2.3 | done | losing for real |
| momentum_60m_0.30pct | 3087 | 49.2 | 49.3 | $-1544.95 | -5.0% | $-544.95 | -2.8 | done | losing for real |
| reversal_60m_0.30pct | 3087 | 50.8 | 51.0 | $-1573.10 | -5.1% | $-573.10 | -2.9 | done | losing for real |
| trend_filter | 2187 | 48.7 | 50.3 | $-1869.39 | -8.5% | $-869.39 | -4.1 | done | losing for real |
| coinflip | 5304 | 50.0 | 50.0 | $-2293.69 | -4.3% | $-1293.69 | -3.2 | done | losing for real |
| momentum_15m_0.10pct | 3675 | 49.1 | 50.2 | $-2301.28 | -6.3% | $-1301.28 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 5304 | 50.2 | 51.3 | $-3299.85 | -6.2% | $-2299.85 | -4.7 | done | losing for real |
| always_up | 5304 | 48.0 | 49.2 | $-3609.97 | -6.8% | $-2609.97 | -4.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 9435 | 48.0 | 48.7 | $-5191.86 |
| ETH | 10130 | 48.0 | 48.0 | $-5677.11 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
