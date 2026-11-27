# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 27, 1:15 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1557 windows, 38195 settled trades, 426 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 790 | 34.2 | 35.3 | $-633.30 | -8.0% | $366.70 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 3784 | 50.9 | 50.0 | $-992.20 | -2.6% | $7.80 | -1.6 | done | can't tell from luck |
| value_ev10 | 1883 | 38.3 | 39.1 | $-1059.10 | -5.6% | $-59.10 | -2.0 | done | can't tell from luck |
| value_ev5 | 2830 | 40.4 | 41.0 | $-1482.75 | -5.2% | $-482.75 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 3178 | 50.9 | 50.9 | $-1536.10 | -4.8% | $-536.10 | -2.8 | done | losing for real |
| momentum_60m_0.30pct | 3178 | 49.1 | 49.2 | $-1655.05 | -5.2% | $-655.05 | -2.9 | done | losing for real |
| trend_filter | 2256 | 48.7 | 50.3 | $-1921.52 | -8.5% | $-921.52 | -4.1 | done | losing for real |
| momentum_15m_0.10pct | 3784 | 49.1 | 50.2 | $-2334.05 | -6.2% | $-1334.05 | -3.8 | done | losing for real |
| coinflip | 5504 | 50.0 | 49.9 | $-2376.11 | -4.3% | $-1376.11 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 5504 | 50.2 | 51.3 | $-3406.12 | -6.2% | $-2406.12 | -4.7 | done | losing for real |
| always_up | 5504 | 48.2 | 49.2 | $-3561.83 | -6.5% | $-2561.83 | -4.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 10051 | 47.9 | 48.6 | $-5817.89 |
| ETH | 10834 | 48.1 | 47.8 | $-5556.00 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
