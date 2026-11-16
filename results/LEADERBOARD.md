# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 16, 3:15 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 509 windows, 14025 settled trades, 65 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 264 | 34.5 | 35.5 | $-178.91 | -6.8% | $821.09 | -0.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 1189 | 51.0 | 49.8 | $-224.37 | -1.9% | $775.63 | -0.6 | done | can't tell from luck |
| value_ev10 | 659 | 38.1 | 39.7 | $-500.51 | -7.6% | $499.49 | -1.6 | done | can't tell from luck |
| trend_filter | 822 | 49.4 | 50.7 | $-570.35 | -6.9% | $429.65 | -2.0 | done | losing for real |
| momentum_15m_0.10pct | 1421 | 49.6 | 49.6 | $-598.24 | -4.2% | $401.76 | -1.6 | done | can't tell from luck |
| value_ev5 | 976 | 40.0 | 41.5 | $-713.88 | -7.3% | $286.12 | -2.0 | done | can't tell from luck |
| reversal_15m_0.10pct | 1421 | 50.4 | 51.6 | $-930.64 | -6.5% | $69.36 | -2.5 | done | losing for real |
| coinflip | 2028 | 50.0 | 50.7 | $-1069.99 | -5.3% | $-69.99 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 1189 | 49.0 | 51.4 | $-1072.95 | -9.0% | $-72.95 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 2028 | 49.6 | 51.6 | $-1539.12 | -7.6% | $-539.12 | -3.5 | done | losing for real |
| always_up | 2028 | 46.3 | 50.1 | $-2374.90 | -11.7% | $-1374.90 | -5.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3172 | 47.4 | 49.2 | $-2539.98 |
| ETH | 3504 | 48.0 | 48.7 | $-2289.28 |
| SOL | 3656 | 47.6 | 49.0 | $-2794.00 |
| XRP | 3693 | 48.3 | 48.8 | $-2150.59 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
