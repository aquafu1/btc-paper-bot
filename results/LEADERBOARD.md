# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 15, 6:05 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 472 windows, 12941 settled trades, 57 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 238 | 35.3 | 35.9 | $-125.26 | -5.3% | $874.74 | -0.6 | done | can't tell from luck |
| momentum_60m_0.30pct | 1094 | 50.8 | 50.0 | $-278.93 | -2.5% | $721.07 | -0.9 | done | can't tell from luck |
| value_ev10 | 612 | 39.4 | 40.2 | $-324.93 | -5.3% | $675.07 | -1.1 | done | can't tell from luck |
| value_ev5 | 905 | 41.3 | 41.9 | $-447.62 | -4.9% | $552.38 | -1.3 | done | can't tell from luck |
| trend_filter | 750 | 49.6 | 50.8 | $-471.85 | -6.3% | $528.15 | -1.8 | done | can't tell from luck |
| momentum_15m_0.10pct | 1304 | 49.9 | 50.0 | $-482.41 | -3.7% | $517.59 | -1.3 | done | can't tell from luck |
| reversal_15m_0.10pct | 1304 | 50.1 | 51.4 | $-853.49 | -6.5% | $146.51 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 1094 | 49.2 | 51.4 | $-936.21 | -8.6% | $63.79 | -2.9 | done | losing for real |
| coinflip | 1880 | 49.8 | 50.8 | $-1071.98 | -5.7% | $-71.98 | -2.5 | done | losing for real |
| momentum_5m_0.00pct | 1880 | 49.7 | 51.7 | $-1355.64 | -7.2% | $-355.64 | -3.2 | done | losing for real |
| always_up | 1880 | 46.7 | 50.4 | $-2063.48 | -11.0% | $-1063.48 | -4.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2927 | 47.5 | 49.3 | $-2233.39 |
| ETH | 3242 | 48.1 | 48.9 | $-2102.94 |
| SOL | 3369 | 47.8 | 49.3 | $-2456.40 |
| XRP | 3403 | 48.8 | 49.1 | $-1619.04 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
