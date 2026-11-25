# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 25, 11:35 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1406 windows, 36190 settled trades, 407 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 726 | 34.8 | 35.3 | $-452.49 | -6.2% | $547.51 | -1.3 | done | can't tell from luck |
| value_ev10 | 1753 | 39.0 | 39.2 | $-724.58 | -4.1% | $275.42 | -1.4 | done | can't tell from luck |
| reversal_15m_0.10pct | 3618 | 50.8 | 50.1 | $-1046.70 | -2.9% | $-46.70 | -1.7 | done | can't tell from luck |
| value_ev5 | 2644 | 40.7 | 41.1 | $-1189.77 | -4.5% | $-189.77 | -2.0 | done | can't tell from luck |
| momentum_60m_0.30pct | 3036 | 49.3 | 49.3 | $-1457.78 | -4.8% | $-457.78 | -2.6 | done | losing for real |
| reversal_60m_0.30pct | 3036 | 50.7 | 51.0 | $-1564.09 | -5.2% | $-564.09 | -2.9 | done | losing for real |
| trend_filter | 2150 | 48.5 | 50.4 | $-1895.58 | -8.8% | $-895.58 | -4.2 | done | losing for real |
| momentum_15m_0.10pct | 3618 | 49.2 | 50.2 | $-2186.16 | -6.0% | $-1186.16 | -3.7 | done | losing for real |
| coinflip | 5203 | 50.0 | 50.0 | $-2253.39 | -4.3% | $-1253.39 | -3.1 | done | losing for real |
| momentum_5m_0.00pct | 5203 | 50.1 | 51.3 | $-3239.41 | -6.2% | $-2239.41 | -4.6 | done | losing for real |
| always_up | 5203 | 47.9 | 49.3 | $-3635.39 | -7.0% | $-2635.39 | -5.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 9090 | 48.1 | 48.8 | $-4801.62 |
| ETH | 9790 | 48.0 | 48.0 | $-5259.48 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
