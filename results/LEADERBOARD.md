# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 15, 8:50 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 435 windows, 11952 settled trades, 77 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 218 | 33.9 | 36.1 | $-214.42 | -9.8% | $785.58 | -1.1 | done | can't tell from luck |
| momentum_60m_0.30pct | 1018 | 51.0 | 50.0 | $-239.06 | -2.3% | $760.94 | -0.8 | done | can't tell from luck |
| trend_filter | 685 | 49.9 | 50.7 | $-391.87 | -5.7% | $608.13 | -1.5 | done | can't tell from luck |
| value_ev10 | 560 | 38.8 | 40.2 | $-415.64 | -7.4% | $584.36 | -1.5 | done | can't tell from luck |
| value_ev5 | 837 | 41.1 | 42.0 | $-501.13 | -6.0% | $498.87 | -1.5 | done | can't tell from luck |
| momentum_15m_0.10pct | 1210 | 49.6 | 50.1 | $-570.46 | -4.7% | $429.54 | -1.6 | done | can't tell from luck |
| coinflip | 1732 | 50.5 | 50.9 | $-799.17 | -4.6% | $200.83 | -2.0 | done | can't tell from luck |
| reversal_15m_0.10pct | 1210 | 50.4 | 51.6 | $-808.85 | -6.7% | $191.15 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 1018 | 49.0 | 51.8 | $-977.25 | -9.6% | $22.75 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 1732 | 49.7 | 51.6 | $-1278.65 | -7.4% | $-278.65 | -3.2 | done | losing for real |
| always_up | 1732 | 46.0 | 50.4 | $-2187.59 | -12.6% | $-1187.59 | -5.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2699 | 47.5 | 49.3 | $-2123.83 |
| ETH | 3000 | 48.0 | 48.9 | $-1948.80 |
| SOL | 3103 | 47.8 | 49.3 | $-2484.09 |
| XRP | 3150 | 48.6 | 49.3 | $-1827.36 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
