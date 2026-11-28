# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 28, 12:15 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1649 windows, 39356 settled trades, 389 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 838 | 34.4 | 35.2 | $-623.68 | -7.4% | $376.32 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 3869 | 50.8 | 49.9 | $-1011.20 | -2.6% | $-11.20 | -1.6 | done | can't tell from luck |
| value_ev10 | 1978 | 38.3 | 39.0 | $-1122.71 | -5.7% | $-122.71 | -2.1 | done | losing for real |
| reversal_60m_0.30pct | 3239 | 51.1 | 50.9 | $-1456.51 | -4.5% | $-456.51 | -2.6 | done | losing for real |
| value_ev5 | 2955 | 40.3 | 41.0 | $-1585.41 | -5.4% | $-585.41 | -2.5 | done | losing for real |
| momentum_60m_0.30pct | 3239 | 48.9 | 49.3 | $-1792.51 | -5.5% | $-792.51 | -3.1 | done | losing for real |
| trend_filter | 2305 | 48.4 | 50.4 | $-2084.47 | -9.0% | $-1084.47 | -4.4 | done | losing for real |
| momentum_15m_0.10pct | 3869 | 49.2 | 50.2 | $-2372.58 | -6.1% | $-1372.58 | -3.8 | done | losing for real |
| coinflip | 5688 | 49.9 | 49.9 | $-2525.31 | -4.4% | $-1525.31 | -3.4 | done | losing for real |
| momentum_5m_0.00pct | 5688 | 50.2 | 51.3 | $-3523.18 | -6.2% | $-2523.18 | -4.8 | done | losing for real |
| always_up | 5688 | 48.2 | 49.0 | $-3553.50 | -6.2% | $-2553.50 | -4.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 10583 | 47.9 | 48.5 | $-5984.80 |
| ETH | 11463 | 47.9 | 47.6 | $-6082.00 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
