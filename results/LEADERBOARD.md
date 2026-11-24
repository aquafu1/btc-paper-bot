# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 23, 7:15 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1245 windows, 33827 settled trades, 412 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 664 | 34.2 | 35.3 | $-514.16 | -7.7% | $485.84 | -1.5 | done | can't tell from luck |
| value_ev10 | 1621 | 38.5 | 39.2 | $-870.67 | -5.4% | $129.33 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 3392 | 50.9 | 50.3 | $-1050.81 | -3.1% | $-50.81 | -1.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 2835 | 49.5 | 49.4 | $-1325.10 | -4.7% | $-325.10 | -2.5 | done | losing for real |
| value_ev5 | 2448 | 40.3 | 41.1 | $-1334.34 | -5.5% | $-334.34 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 2835 | 50.5 | 51.1 | $-1644.51 | -5.8% | $-644.51 | -3.2 | done | losing for real |
| trend_filter | 2000 | 48.6 | 50.4 | $-1723.24 | -8.6% | $-723.24 | -3.9 | done | losing for real |
| momentum_15m_0.10pct | 3392 | 49.1 | 50.2 | $-2155.86 | -6.4% | $-1155.86 | -3.7 | done | losing for real |
| coinflip | 4880 | 50.1 | 50.1 | $-2170.08 | -4.4% | $-1170.08 | -3.1 | done | losing for real |
| momentum_5m_0.00pct | 4880 | 50.2 | 51.4 | $-2996.12 | -6.1% | $-1996.12 | -4.4 | done | losing for real |
| always_up | 4880 | 47.8 | 49.3 | $-3592.18 | -7.4% | $-2592.18 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7944 | 47.9 | 48.9 | $-4778.23 |
| ETH | 8573 | 48.1 | 48.3 | $-5014.61 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
