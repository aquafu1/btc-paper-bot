# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 14, 12:30 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 354 windows, 9528 settled trades, 64 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 185 | 37.3 | 36.6 | $-48.35 | -2.6% | $951.65 | -0.3 | Sat 8:00 PM | too few trades (185/200) |
| value_ev10 | 458 | 40.2 | 40.3 | $-186.10 | -4.1% | $813.90 | -0.7 | done | can't tell from luck |
| value_ev5 | 682 | 41.6 | 42.0 | $-326.09 | -4.8% | $673.91 | -1.1 | done | can't tell from luck |
| reversal_15m_0.10pct | 946 | 52.1 | 52.1 | $-391.11 | -4.1% | $608.89 | -1.3 | done | can't tell from luck |
| reversal_60m_0.30pct | 780 | 51.3 | 51.9 | $-410.41 | -5.3% | $589.59 | -1.5 | done | can't tell from luck |
| trend_filter | 527 | 48.0 | 50.4 | $-480.19 | -9.1% | $519.81 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 780 | 48.7 | 49.7 | $-504.30 | -6.5% | $495.70 | -1.8 | done | can't tell from luck |
| momentum_15m_0.10pct | 946 | 47.9 | 49.7 | $-723.86 | -7.7% | $276.14 | -2.4 | done | losing for real |
| coinflip | 1408 | 50.1 | 50.8 | $-741.98 | -5.3% | $258.02 | -2.0 | done | losing for real |
| momentum_5m_0.00pct | 1408 | 49.4 | 51.5 | $-1078.74 | -7.7% | $-78.74 | -3.0 | done | losing for real |
| always_up | 1408 | 46.6 | 50.6 | $-1653.11 | -11.7% | $-653.11 | -4.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2135 | 47.3 | 49.3 | $-1716.87 |
| ETH | 2400 | 47.6 | 48.7 | $-1756.26 |
| SOL | 2469 | 48.1 | 49.4 | $-1805.40 |
| XRP | 2524 | 48.9 | 49.1 | $-1265.72 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
